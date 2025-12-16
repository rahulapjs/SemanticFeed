import type { Story } from '../types';
import { SourceItem } from './SourceItem';
import styles from './StoryCard.module.css';

interface StoryCardProps {
    story: Story;
}

export const StoryCard = ({ story }: StoryCardProps) => {
    return (
        <article className={styles.card}>
            <h2 className={styles.title}>{story.title}</h2>
            {story.summary && (
                <p className={styles.summaryText}>{story.summary}</p>
            )}
            <div className={styles.sources}>
                {story.sources.map((source, index) => (
                    <SourceItem key={index} source={source} />
                ))}
            </div>
        </article>
    );
};
