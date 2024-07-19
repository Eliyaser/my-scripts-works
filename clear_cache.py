import os
import shutil
import platform

def clear_chrome_cache():
    # Define the paths for different operating systems
    paths = {
        'Windows': os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'Cache'),
        'Darwin': os.path.join(os.getenv('HOME'), 'Library', 'Caches', 'Google', 'Chrome', 'Default', 'Cache'),
        'Linux': os.path.join(os.getenv('HOME'), '.cache', 'google-chrome', 'Default', 'Cache')
    }

    # Get the current operating system
    current_os = platform.system()

    # Get the cache path based on the OS
    cache_path = paths.get(current_os)

    if not cache_path:
        print(f"Unsupported OS: {current_os}")
        return

    # Check if the cache path exists
    if os.path.exists(cache_path):
        # Delete the cache folder
        try:
            shutil.rmtree(cache_path)
            print(f"Successfully cleared the cache for Chrome on {current_os}")
        except Exception as e:
            print(f"Error clearing cache: {e}")
    else:
        print("Cache path does not exist")

# Run the function to clear the Chrome cache
clear_chrome_cache()
