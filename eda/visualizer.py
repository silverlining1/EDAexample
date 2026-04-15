"""Chart generation using matplotlib and seaborn."""

import logging
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import config

logger = logging.getLogger(__name__)

sns.set_theme(style="whitegrid", palette="muted")


def visualize_data(df: pd.DataFrame, results: dict, output_dir: str) -> list[str]:
    """Generate and save all charts. Returns list of saved file paths.

    Args:
        df: Cleaned DataFrame.
        results: Analysis results dict from analyzer.
        output_dir: Directory to save chart files.

    Returns:
        List of paths to saved chart files.
    """
    chart_paths = []

    # Chart 1: Videos per day
    if "videos_per_day" in results and not results["videos_per_day"].empty:
        path = _plot_videos_per_day(results["videos_per_day"], output_dir)
        if path:
            chart_paths.append(path)

    # Chart 2: Duration distribution
    if config.DURATION_COLUMN in df.columns and not df[config.DURATION_COLUMN].dropna().empty:
        path = _plot_duration_distribution(df, output_dir)
        if path:
            chart_paths.append(path)

    # Chart 3: Top pages
    if "top_pages" in results and not results["top_pages"].empty:
        path = _plot_top_pages(results["top_pages"], output_dir)
        if path:
            chart_paths.append(path)

    logger.info(f"Generated {len(chart_paths)} chart(s)")
    return chart_paths


def _plot_videos_per_day(videos_per_day: pd.Series, output_dir: str) -> str | None:
    try:
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(videos_per_day.index, videos_per_day.values, linewidth=2, color="#2196F3")
        ax.fill_between(videos_per_day.index, videos_per_day.values, alpha=0.15, color="#2196F3")
        ax.set_title("Videos Published per Day", fontsize=14, fontweight="bold", pad=12)
        ax.set_xlabel("Date")
        ax.set_ylabel("Number of Videos")
        plt.xticks(rotation=45)
        plt.tight_layout()
        path = os.path.join(output_dir, "videos_per_day.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        logger.info(f"Saved chart: {path}")
        return path
    except Exception as e:
        logger.error(f"Failed to generate videos_per_day chart: {e}")
        return None


def _plot_duration_distribution(df: pd.DataFrame, output_dir: str) -> str | None:
    try:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(df[config.DURATION_COLUMN].dropna(), kde=True, ax=ax, color="#4CAF50")
        ax.set_title("Distribution of Video Durations", fontsize=14, fontweight="bold", pad=12)
        ax.set_xlabel("Duration (seconds)")
        ax.set_ylabel("Count")
        plt.tight_layout()
        path = os.path.join(output_dir, "duration_distribution.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        logger.info(f"Saved chart: {path}")
        return path
    except Exception as e:
        logger.error(f"Failed to generate duration_distribution chart: {e}")
        return None


def _plot_top_pages(top_pages: pd.Series, output_dir: str) -> str | None:
    try:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=top_pages.values, y=top_pages.index, ax=ax, palette="Blues_d")
        ax.set_title(f"Top {len(top_pages)} Pages by Video Count", fontsize=14, fontweight="bold", pad=12)
        ax.set_xlabel("Number of Videos")
        ax.set_ylabel("Page Name")
        plt.tight_layout()
        path = os.path.join(output_dir, "top_pages.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        logger.info(f"Saved chart: {path}")
        return path
    except Exception as e:
        logger.error(f"Failed to generate top_pages chart: {e}")
        return None
