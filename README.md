
# Wi-Fi File Transfer Application

A lightweight and efficient cross-platform desktop application for transferring files over a local Wi-Fi connection. The application combines a PyQt6-based graphical user interface with a Flask-based HTTP server to enable secure file uploads and downloads via any device connected to the same network.

---

## Features

- Modern, dark-themed GUI built with PyQt6
- Upload files from any device via browser (desktop, Android, iOS)
- Browse and download uploaded files through a dedicated web interface
- Real-time upload progress indicator
- Server status display with auto IP detection
- Start/Stop server control via GUI
- Responsive HTML/CSS web pages optimized for both desktop and mobile devices

---

## Requirements

- Python 3.9 or higher
- Required dependencies:
  ```bash
  pip install flask pyqt6
  ```

---

## Usage

1. Clone the repository or download the source files.
2. Run the main script:
   ```bash
   python wifi_transfer.py
   ```
3. In the GUI:
   - Click "Select Folder" to specify a directory for uploaded files.
   - Click "Start Server" to initialize the Flask server.
   - The IP address and upload/download URLs will be displayed.

4. From another device on the same Wi-Fi network:
   - Open a browser and navigate to:
     - Upload page: `<your-ip>:8000`
     - Download page: `<your-ip>:8000/browse`

---

## Important Notes for Proper Operation

To ensure reliable file transfer over the local Wi-Fi network, the following conditions must be met:

- **Network Adapter Configuration**:
  - Disable all network interfaces except the one associated with the desired Wi-Fi connection before starting the application.
  - This avoids routing conflicts and ensures the correct IP is selected.

- **Administrator Privileges**:
  - The application must be run with administrative privileges.
  - If compiled into an executable, it is preconfigured to request elevation on launch.

- **DHCP Network Considerations**:
  - If your Wi-Fi network uses **DHCP**, assign **manual (static)** IP addresses to the mobile devices within the same IP range.

- **Static IP Configuration**:
  - If your computer uses a **static IP**, ensure a valid **gateway address** is defined in its network settings.
  - On mobile devices, manually set an IP in the same subnet as the computer.


---

## Author

Developed by Sasan Zare  
Version 2.0
---
---

The birth of this application comes with a story—and in the following section, I’ll be sharing that story with you.

---
# The Story

In the world of medical imaging installation and after-sales service, every second counts. This Application was born out of the chaos of installing and licensing software for medical imaging devices in environments where technology often feels like an adversary. Picture this: you're at a remote hospital or clinic, tasked with setting up critical software on a computer. The catch? You need to send a system ID (a humble .txt file) to the vendor and receive license files (.dat and .key) in return. Sounds simple—until you realize there's no internet, barely any mobile signal, and your iPhone can't transfer files via cable.

This was my reality. For years, I relied on makeshift solutions: using my iPhone's hotspot to connect to WhatsApp or Telegram's web versions, transferring files over shaky EDGE or GPRS connections. It worked—sometimes—but it was slow, unreliable, and a constant source of frustration. One day, while staring at yet another "No Internet Connection" error, an idea sparked: What if I could transfer files over Wi-Fi without needing an internet connection?

That’s how This Application came to life. I set out to build a lightweight Windows application that could transfer files seamlessly between my iPhone and a computer using a local Wi-Fi network. No internet, no cables, just a USB Wi-Fi dongle and my iPhone’s hotspot. The goal was simple: make the process fast, reliable, and stress-free.

Building This Application wasn’t without its hurdles. From figuring out how to establish a stable local network connection to optimizing the app for minimal resource usage, every step was a lesson in problem-solving. I wanted it to be plug-and-play—copy the app from a USB drive, plug in a Wi-Fi dongle, connect to the iPhone hotspot, and transfer files, even in the most remote locations. After countless late nights and iterations, This Application became exactly that: a tool that saves time and brings peace of mind.

Now, wherever I go, This Application is my trusty companion. It’s not just about moving files; it’s about making critical installations smoother, ensuring medical professionals can focus on their work without tech headaches. Whether you’re in a high-tech hospital or a clinic with spotty signal, This Application is here to bridge the gap—one file at a time.

Try it out, and let me know how it streamlines your workflow. Here’s to solving real-world problems with a bit of code and a lot of determination.

---
### If you have any ideas to improve or enhance this application, feel free to share them with me. I’m all ears — I’ll do my best to build it for you and make it available. Let’s combine creativity, ingenuity, and a whole lot of determination to solve real-world problems, one line of code at a time.
