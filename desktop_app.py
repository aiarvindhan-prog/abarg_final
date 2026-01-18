import webview
import sys

# Hide console for GUI app
if getattr(sys, 'frozen', False):
    import pyi_splash

if __name__ == '__main__':
    # Close splash screen if it exists
    if getattr(sys, 'frozen', False) and 'pyi_splash' in sys.modules:
        pyi_splash.close()

    # Create window pointing to the live server
    # REPLACE 'https://your-new-app-name.onrender.com' with your actual new Render URL
    webview.create_window('ABARG Chat', 'https://your-new-app-name.onrender.com', width=1200, height=800, resizable=True)
    
    # Start webview
    webview.start()
