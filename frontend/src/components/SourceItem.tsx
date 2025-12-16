import { ExternalLink } from 'lucide-react';
import { formatDistanceToNow } from 'date-fns';
import type { Source } from '../types';
import styles from './SourceItem.module.css';

interface SourceItemProps {
    source: Source;
}

export const SourceItem = ({ source }: SourceItemProps) => {
    let timeAgo = '';
    try {
        timeAgo = formatDistanceToNow(new Date(source.timestamp), { addSuffix: true });
    } catch {
        timeAgo = 'recently';
    }

    return (
        <div className={styles.container}>
            <span className={styles.name}>{source.name}</span>
            <span className={styles.dot}>•</span>
            <span className={styles.time}>{timeAgo}</span>
            <a href={source.url} target="_blank" rel="noopener noreferrer" className={styles.link} aria-label={`Read on ${source.name}`}>
                <ExternalLink size={14} />
            </a>
        </div>
    );
};
