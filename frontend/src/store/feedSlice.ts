import { createSlice, createAsyncThunk, type PayloadAction } from '@reduxjs/toolkit';
import type { Story, FeedResponse } from '../types';

interface FeedState {
    stories: Story[];
    loading: boolean;
    error: string | null;
}

const initialState: FeedState = {
    stories: [],
    loading: false,
    error: null,
};

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

export const fetchFeed = createAsyncThunk('feed/fetchFeed', async () => {
    const response = await fetch(`${API_BASE_URL}/feed`);
    if (!response.ok) {
        throw new Error(`Failed to fetch feed: ${response.statusText}`);
    }
    const data: FeedResponse = await response.json();
    const mappedStories = data.map((item) => {
        const sources = item.sources.map((source) => ({
            name: source.source,
            url: source.url,
            timestamp: source.published_at,
        }));

        // Find the most recent timestamp among sources, or default to epoch if none
        // We assume ISO strings which sort lexicographically correctly, but converting to Date is safer for diffs
        const latestTimestamp = sources.reduce((latest, current) => {
            return current.timestamp > latest ? current.timestamp : latest;
        }, sources[0]?.timestamp || new Date(0).toISOString());

        return {
            id: item.story_id,
            title: item.title,
            summary: item.summary,
            sources,
            latestTimestamp
        };
    });

    // Sort by latest first
    return mappedStories.sort((a, b) =>
        new Date(b.latestTimestamp).getTime() - new Date(a.latestTimestamp).getTime()
    );
});

const feedSlice = createSlice({
    name: 'feed',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchFeed.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(fetchFeed.fulfilled, (state, action: PayloadAction<Story[]>) => {
                state.loading = false;
                state.stories = action.payload;
            })

            .addCase(fetchFeed.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message || 'Something went wrong';
            });
    },
});

export default feedSlice.reducer;
