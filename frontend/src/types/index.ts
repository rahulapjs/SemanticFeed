export interface Source {
    name: string;
    url: string;
    timestamp: string;
}

export interface Story {
    id: number;
    title: string;
    summary: string | null;
    sources: Source[];
    latestTimestamp: string;
}

export interface ApiSource {
    source: string;
    url: string;
    published_at: string;
}

export interface ApiStory {
    story_id: number;
    title: string;
    summary: string | null;
    sources: ApiSource[];
}

export type FeedResponse = ApiStory[];
