<!-- Improved compatibility of back to top link: See: https://github.com/xwnb/GitGeminiHub/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the GitGeminiHub. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/xwnb/GitGeminiHub">
<!--     <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

<h1 align="center">GitGeminiHub</h1>

  <p align="center">
    I'm GitGeminiHub - inspired and empowered by Gemini and GitHub Actions
    <br />
    <a href="https://github.com/xwnb/GitGeminiHub"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/xwnb/GitGeminiHub">View Demo</a>
    ·
    <a href="https://github.com/xwnb/GitGeminiHub/issues">Report Bug</a>
    ·
    <a href="https://github.com/xwnb/GitGeminiHub/issues">Request Feature</a>
  </p>
</div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![If useful][if-useful-shield]][if-useful-url]
[![Stargazers][stars-shield]][stars-url]
[![Forks][forks-shield]][forks-url]
[![Contributors][contributors-shield]][contributors-url]
[![Docs site](https://img.shields.io/badge/docs-GitHub_Pages-blue)](https://xwnb.github.io/)
[![MIT License][license-shield]][license-url]

[![Issues][issues-shield]][issues-url]
[![GitHub issues closed](https://img.shields.io/github/issues-closed/xwnb/GitGeminiHub)](https://github.com/xwnb/GitGeminiHub/issues?q=is%3Aissue+sort%3Aupdated-desc+is%3Aopen)
[![Pull requests][pull-requests-shield]][pull-requests-url]
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/xwnb/GitGeminiHub)

[![GitHub last commit](https://img.shields.io/github/last-commit/xwnb/GitGeminiHub)](https://github.com/xwnb/GitGeminiHub)
[![GitHub commit activity weekly](https://img.shields.io/github/commit-activity/w/xwnb/GitGeminiHub)](https://github.com/xwnb/GitGeminiHub/graphs/commit-activity)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/xwnb/GitGeminiHub/translator.yml)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
<!--         <li><a href="#installation">Installation</a></li> -->
        <li><a href="#steps">Steps</a></li>
      </ul>
    </li>
<!--     <li><a href="#usage">Usage</a></li> -->
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is GitGeminiHub built by [GitHub Action](https://github.com/features/actions) and [Google Gemini](https://deepmind.google/technologies/gemini/#introduction) API to response automatically by submitting Issues. ***It is a learning, open-source project. If any complains, please contact me.***

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



### Built With

* [**GitHub Action**](https://github.com/features/actions): Automate your workflow
from idea to production
* [**Google Gemini**](https://deepmind.google/technologies/gemini/#introduction): Welcome to
the Gemini
 era

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- GETTING STARTED -->
## Getting Started

Follow the steps learn how to submit a translation task.

### Prerequisites

For developers or contributors who folk as a personal project:

1. [Fork repository](https://github.com/xwnb/GitGeminiHub/fork) as your owners
2. [Get an API key](https://makersuite.google.com/app/apikey)
3. **Add the Gemini API key in project setting**
  - **Settting** -> **Security**/**Secrets and variables**/**Actions** -> **Secrets**/**Repository secrets**

For users:

1. **You need a GitHub account and should better know how to use GitHub, like create an issue.**
2. [Open Issue](https://github.com/xwnb/GitGeminiHub/issues) to create a [New issue](https://github.com/xwnb/GitGeminiHub/issues/new/choose) ticket


<!--
### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/xwnb/GitGeminiHub.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- USAGE EXAMPLES -->
### Steps

1. [Open Issue](https://github.com/xwnb/GitGeminiHub/issues) to create a [New issue](https://github.com/xwnb/GitGeminiHub/issues/new/choose) ticket
2. Choose any **task request** to start submitting a task issue
3. Fill the prompt you want task to execute in **### Prompt** section
4. Fill the content (upload/drop files or images or their links) in **### Content** section
5. Submit the new issue
6. Wait the task finished.
7. Check the new comment added by action bot

**The result will be post at the issue page by bot comment. If task failed, please check the issue description, edit or reopen or re-create can re-trigger the translation task automatically.**

<!-- _For more examples, please refer to the [Documentation](https://github.com/xwnb/GitGeminiHub/blob/main/README.md)_ -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ROADMAP -->
## Roadmap

- [x] Build with GitHub Action and Gemini API triggered by Issue event
- [x] Support *.txt, *.md files for translation
- [x] Support image file for prompting
- [x] Post response by Issue comment.
- [x] Add configuration section for Gemini setting in Issue template
- [ ] Support other plain text formats
- [ ] Support `*.pdf`
- [ ] Support OCR for images, scanned-documents
- [ ] Notify task result to users by email
- [ ] ...

See the [open issues]() for a full list of proposed features (and known issues).

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

<!-- Your Name - [@twitter_handle](xxx) - email@xxx.com -->

Project Link: [https://github.com/xwnb/GitGeminiHub](https://github.com/xwnb/GitGeminiHub)

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [GitHub Action: Automate your workflow
from idea to production](https://github.com/features/actions)
* [Google Gemini: Welcome to
the Gemini
 era](https://deepmind.google/technologies/gemini/#introduction)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/xwnb/GitGeminiHub?color=cca4e3
[contributors-url]: https://github.com/xwnb/GitGeminiHub/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/xwnb/GitGeminiHub?color=
[forks-url]: https://github.com/xwnb/GitGeminiHub/network/members
[stars-shield]: https://img.shields.io/github/stars/xwnb/GitGeminiHub?color=4b5cc4
[stars-url]: https://github.com/xwnb/GitGeminiHub/stargazers
[issues-shield]: https://img.shields.io/github/issues/xwnb/GitGeminiHub?color=f00056
[issues-url]: https://github.com/xwnb/GitGeminiHub/issues
[pull-requests-shield]: https://img.shields.io/github/issues-pr/xwnb/GitGeminiHub?color=ff8c31
[pull-requests-url]: https://github.com/xwnb/GitGeminiHub/pulls
[license-shield]: https://img.shields.io/github/license/xwnb/GitGeminiHub?color=827100
[license-url]: https://github.com/xwnb/GitGeminiHub/blob/main/LICENSE
[product-screenshot]: images/screenshot.png
[if-useful-shield]: https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99
[if-useful-url]: https://github.com/xwnb/GitGeminiHub
