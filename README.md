<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">SCREEN-TRANSLATE</h1></p>
<p align="center">
	<!--<img src="https://img.shields.io/github/license/zsoltdzsugan/screen-translate?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license"> -->
	<img src="https://img.shields.io/github/last-commit/zsoltdzsugan/screen-translate?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/zsoltdzsugan/screen-translate?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/zsoltdzsugan/screen-translate?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)

---

##  Overview

This project translates text from a captured screen area to a different language (for now it translates only to Hungarian). It is a small project to familiarize myself with python.
I used openai (chatgpt api) for translation, the GPT3.5 model. For img-to-text extraction i used pytesseract.
---

##  Features

From a screen-capture extracts the text and translates it to Hungarian.

---

##  Project Structure

```sh
└── screen-translate/
    ├── Dockerfile
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── app_class.py
    │   ├── gui.py
    │   └── screenshot_class.py
    ├── main.py
    ├── requirements.txt
    └── services
        ├── ai_translator.py
        ├── screen_capture.py
        └── text_extractor.py
```

---
##  Getting Started

###  Prerequisites

Before getting started with screen-translate, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Install screen-translate using one of the following methods:

**Build from source:**

1. Clone the screen-translate repository:
```sh
❯ git clone https://github.com/zsoltdzsugan/screen-translate
```

2. Navigate to the project directory:
```sh
❯ cd screen-translate
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t zsoltdzsugan/screen-translate .
```




###  Usage
Run screen-translate using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement translation from English to Hungarian.</strike>
- [ ] **`Task 2`**: Implement multiple languages.
- [ ] **`Task 3`**: Implement better design.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/zsoltdzsugan/screen-translate/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/zsoltdzsugan/screen-translate/issues)**: Submit bugs found or log feature requests for the `screen-translate` project.
- **💡 [Submit Pull Requests](https://github.com/zsoltdzsugan/screen-translate/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/zsoltdzsugan/screen-translate
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>
---
