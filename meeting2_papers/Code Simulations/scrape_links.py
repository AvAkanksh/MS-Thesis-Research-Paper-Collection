import re
from bs4 import BeautifulSoup

def extract_all_youtube_info(file_path):
    try:
        # Read the HTML content from the .txt file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # List to store video info
        videos = []

        # Helper function to clean and validate YouTube URL
        def get_youtube_url(url):
            match = re.search(r'(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([\w-]+)', url)
            if match:
                return f"https://www.youtube.com/watch?v={match.group(1)}"
            return None

        # 1. Find YouTube links in iframes (embedded videos)
        for iframe in soup.find_all('iframe', src=re.compile(r'youtube\.com/embed|yout\.be')):
            if 'src' in iframe.attrs:
                youtube_url = get_youtube_url(iframe['src'])
                if youtube_url:
                    # Look for nearby title (e.g., in parent container, preceding h1/h2/h3, or meta)
                    title = None
                    parent = iframe.find_parent()
                    if parent:
                        # Check for h1, h2, h3, or span in parent or nearby
                        for tag in parent.find_all(['h1', 'h2', 'h3', 'span'], recursive=True):
                            if tag.get_text().strip():
                                title = tag.get_text().strip()
                                break
                        # Fallback to meta og:title if no nearby title
                        if not title and soup.find('meta', property='og:title'):
                            title = soup.find('meta', property='og:title')['content'].strip()
                    videos.append({
                        'title': title if title else 'No title found',
                        'youtube_url': youtube_url
                    })

        # 2. Find YouTube links in <a> tags
        for a_tag in soup.find_all('a', href=re.compile(r'youtube\.com/watch\?v=|youtu\.be/')):
            youtube_url = get_youtube_url(a_tag['href'])
            if youtube_url:
                # Look for title in the <a> tag's text or nearby
                title = a_tag.get_text().strip() or None
                if not title:
                    parent = a_tag.find_parent()
                    if parent:
                        for tag in parent.find_all(['h1', 'h2', 'h3', 'span'], recursive=True):
                            if tag.get_text().strip():
                                title = tag.get_text().strip()
                                break
                videos.append({
                    'title': title if title else 'No title found',
                    'youtube_url': youtube_url
                })

        # 3. Fallback: Find YouTube URLs in raw text
        url_pattern = r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[\w-]+)'
        for match in re.finditer(url_pattern, html_content):
            youtube_url = get_youtube_url(match.group(0))
            if youtube_url:
                # No direct title association in raw text, use document title or meta
                title = None
                if soup.title and soup.title.string:
                    title = soup.title.string.strip()
                elif soup.find('meta', property='og:title'):
                    title = soup.find('meta', property='og:title')['content'].strip()
                videos.append({
                    'title': title if title else 'No title found',
                    'youtube_url': youtube_url
                })

        # Remove duplicates by YouTube URL
        seen_urls = set()
        unique_videos = []
        for video in videos:
            if video['youtube_url'] not in seen_urls:
                seen_urls.add(video['youtube_url'])
                unique_videos.append(video)

        # Return results
        if unique_videos:
            return unique_videos
        return [{'error': 'No YouTube videos or titles found in the provided HTML'}]

    except FileNotFoundError:
        return [{'error': 'File not found'}]
    except Exception as e:
        return [{'error': f'An error occurred: {str(e)}'}]

# Example usage
if __name__ == "__main__":
    results = extract_all_youtube_info('input.html.txt')
    for video in results:
        if 'error' in video:
            print("Error:", video['error'])
        else:
            print(f"Title: {video['title']}")
            print(f"YouTube URL: {video['youtube_url']}")
            print("-" * 50)