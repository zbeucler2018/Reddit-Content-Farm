<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Reddit Content Farm</h3>

  <p align="center">
    A program that creates a video of reddit posts and adds a TTS narration of the posts
    <br />
    <a href="https://github.com/zbeucler2018/Reddit-Content-Farm">View Demo</a>
    ·
    <a href="https://github.com/zbeucler2018/Reddit-Content-Farm/issues">Report Bug</a>
    ·
    <a href="https://github.com/zbeucler2018/Reddit-Content-Farm/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have have contributed to expanding this template!

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python 3](https://www.python.org/downloads/)
* [Praw](https://praw.readthedocs.io/en/latest/)




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Make sure pip is up to date.
* pip
  ```sh
  pip install --upgrade pip
  ```
 * Have a Reddit Account

### Installation

1. Create a Reddit `script` App [here](https://www.reddit.com/prefs/apps)
2. Clone the repo
   ```sh
   git clone https://github.com/zbeucler2018/Reddit-Content-Farm.git
   ```
3. Install PIP packages
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your Reddit app's client ID, client secret, and user agent in `Reddit.py`
   ```Python
   reddit = praw.Reddit(client_id="Client ID", client_secret="Client Secret", user_agent="User Agent")
   ```
5. Start the script
   ```sh
   Python main.py
   ```
   


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/zbeucler2018/Reddit-Content-Farm/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [ReadME Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)


## ToDo
- [ ] allow automatic upload to youtube
- [ ] allow user to pick which subreddit to get the posts from
