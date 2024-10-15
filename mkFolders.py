import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QListWidget, QLabel, QHBoxLayout

from PySide6.QtCore import Qt

class MyUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Project directory input
        projLayout = QHBoxLayout()
        proj_dir_label = QLineEdit()
        proj_dir_label.setPlaceholderText("Project Directory")
        projLayout.addWidget(proj_dir_label)
        browse_button = QPushButton("Browse")
        projLayout.addWidget(browse_button)
        

        # Project name input
        projname = QVBoxLayout()
        proj_name_label = QLineEdit()
        proj_name_label.setPlaceholderText("Project Name")
        projname.addWidget(proj_name_label)
        projname.addLayout(projLayout)
        layout.addLayout(projname)

        # Number of shots input
        shotLayout = QHBoxLayout()
        num_shots_label = QLabel("Number of Shots")
        num_shots_spinbox = QSpinBox()
        num_shots_spinbox.setValue(1)
        shotLayout.addWidget(num_shots_label)
        shotLayout.addWidget(num_shots_spinbox)
        layout.addLayout(shotLayout)
        

        # Create a grid layout for the number of assets and asset names
        num_assets = QListWidget()
        assetsLabel = QLabel("Assets")
        assetLayout = QVBoxLayout()
        assetLayout.addWidget(assetsLabel)
        assetLayout.addWidget(num_assets)
        
        # Add asset input and button
        asset_input_layout = QHBoxLayout()
        asset_input = QLineEdit()
        asset_input.setPlaceholderText("Enter asset name")
        add_asset_button = QPushButton("Add Asset")
        
        asset_input_layout.addWidget(asset_input)
        asset_input_layout.addWidget(add_asset_button)
        
        assetLayout.addLayout(asset_input_layout)
        layout.addLayout(assetLayout)
        
        # Connect button to function
        add_asset_button.clicked.connect(lambda: num_assets.addItem(asset_input.text()))

        
      

     

        # Create buttons
        create_folders_button = QPushButton("Create Folders")
        cancel_button = QPushButton("Cancel")

        layout.addWidget(create_folders_button)
        layout.addWidget(cancel_button)

   

    def showUI(self):
        self.show()

app = QApplication(sys.argv)
ui = MyUI()
ui.showUI()
sys.exit(app.exec_())