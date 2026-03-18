import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTextEdit
from scapy.all import sniff

class PacketMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("NetSpecter PRO MAX")
        self.setGeometry(100, 100, 800, 600)
        
        # Layout and Widgets
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Real-Time Network Traffic Monitoring")
        self.layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)
        
        self.start_button = QPushButton("Start Monitoring")
        self.start_button.clicked.connect(self.start_monitoring)
        self.layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton("Stop Monitoring")
        self.stop_button.clicked.connect(self.stop_monitoring)
        self.stop_button.setDisabled(True)
        self.layout.addWidget(self.stop_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
        self.monitoring = False

    def start_monitoring(self):
        self.monitoring = True
        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)
        self.text_edit.clear()
        self.sniff_packets()

    def stop_monitoring(self):
        self.monitoring = False
        self.start_button.setEnabled(True)
        self.stop_button.setDisabled(True)

    def sniff_packets(self):
        sniff(prn=self.process_packet, store=0)

    def process_packet(self, packet):
        if not self.monitoring:
            return
        self.text_edit.append(f"Captured Packet: {packet.summary()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PacketMonitor()
    window.show()
    sys.exit(app.exec_())