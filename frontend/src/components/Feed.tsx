import { useEffect } from 'react';
import { useAppDispatch, useAppSelector } from '../store';
import { fetchFeed } from '../store/feedSlice';
import { StoryCard } from './StoryCard';
import styles from './Feed.module.css';

const SkeletonStory = () => (
    <div className={styles.skeletonCard}>
        <div className={`${styles.skeleton} ${styles.skeletonTitle}`}></div>
        <div className={`${styles.skeleton} ${styles.skeletonLine}`}></div>
        <div className={`${styles.skeleton} ${styles.skeletonLine}`} style={{ width: '80%' }}></div>
        <div className={`${styles.skeleton} ${styles.skeletonFooter}`}></div>
    </div>
);

export const Feed = () => {
    const dispatch = useAppDispatch();
    const { stories, loading, error } = useAppSelector((state) => state.feed);

    useEffect(() => {
        dispatch(fetchFeed());
    }, [dispatch]);

    if (loading && stories.length === 0) {
        return (
            <div className={styles.container}>
                {[1, 2, 3].map((i) => <SkeletonStory key={i} />)}
            </div>
        );
    }

    if (error) {
        return (
            <div className={styles.container}>
                <div className={styles.errorArea}>
                    <p className={styles.errorMessage}>{error}</p>
                    <button onClick={() => dispatch(fetchFeed())} className={styles.retryBtn}>Retry Connection</button>
                </div>
            </div>
        );
    }

    return (
        <main className={styles.container}>
            {stories.length === 0 ? (
                <div className={styles.empty}>No stories found.</div>
            ) : (
                stories.map((story) => (
                    <StoryCard key={story.id} story={story} />
                ))
            )}
        </main>
    );
};
