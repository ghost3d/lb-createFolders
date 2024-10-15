import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QListWidget, QLabel, QHBoxLayout, QFileDialog
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
        self.proj_dir_label = QLineEdit()
        self.proj_dir_label.setPlaceholderText("Project Directory")
        projLayout.addWidget(self.proj_dir_label)
        browse_button = QPushButton("Browse")
        projLayout.addWidget(browse_button)
        browse_button.clicked.connect(self.browse_directory)

        # Project name input
        projname = QVBoxLayout()
        self.proj_name_label = QLineEdit()
        self.proj_name_label.setPlaceholderText("Project Name")
        projname.addWidget(self.proj_name_label)
        projname.addLayout(projLayout)
        layout.addLayout(projname)

        # Number of shots input
        shotLayout = QHBoxLayout()
        num_shots_label = QLabel("Number of Shots")
        self.num_shots_spinbox = QSpinBox()
        self.num_shots_spinbox.setValue(1)
        shotLayout.addWidget(num_shots_label)
        shotLayout.addWidget(self.num_shots_spinbox)
        layout.addLayout(shotLayout)

        # Create a grid layout for the number of assets and asset names
        self.num_assets = QListWidget()
        assetsLabel = QLabel("Assets")
        assetLayout = QVBoxLayout()
        assetLayout.addWidget(assetsLabel)
        assetLayout.addWidget(self.num_assets)

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
        add_asset_button.clicked.connect(lambda: self.num_assets.addItem(asset_input.text()))

        # Create buttons
        create_folders_button = QPushButton("Create Folders")
        cancel_button = QPushButton("Cancel")
        create_folders_button.clicked.connect(self.create_folders)

        layout.addWidget(create_folders_button)
        layout.addWidget(cancel_button)

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if directory:
            self.proj_dir_label.setText(directory)

    def create_folders(self):
        project_dir = self.proj_dir_label.text()
        project_name = self.proj_name_label.text()
        num_shots = self.num_shots_spinbox.value()
        asset_items = [self.num_assets.item(i).text() for i in range(self.num_assets.count())]

        if not project_dir or not project_name:
            print("Project directory and name must be specified.")
            return

        root_path = Path(project_dir) / project_name
        root_path.mkdir(parents=True, exist_ok=True)

        # Create main folders
        for folder in ["_config", "shots", "assets", "_ref", "_edit"]:
            (root_path / folder).mkdir(exist_ok=True)

        # Create shot folders
        shots_path = root_path / "shots"
        for i in range(1, num_shots + 1):
            shot_folder = shots_path / f"Shot{i:03d}"
            shot_folder.mkdir(exist_ok=True)
            (shot_folder / "work").mkdir(exist_ok=True)
            (shot_folder / "render").mkdir(exist_ok=True)

        # Create asset folders
        assets_path = root_path / "assets"
        for asset in asset_items:
            asset_folder = assets_path / asset
            asset_folder.mkdir(exist_ok=True)
            (asset_folder / "work").mkdir(exist_ok=True)
            (asset_folder / "publish").mkdir(exist_ok=True)

        print(f"Folders created successfully in {root_path}")


    

    def showUI(self):
        self.show()

app = QApplication(sys.argv)
ui = MyUI()
ui.showUI()
sys.exit(app.exec_())
