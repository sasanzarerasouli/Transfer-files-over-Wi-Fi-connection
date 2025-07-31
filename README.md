
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
     - Upload page: `http://<your-ip>:8000`
     - Download page: `http://<your-ip>:8000/browse`

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

