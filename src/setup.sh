sudo easy_install pip
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install ffmpeg
brew link ffmpeg
brew tap homebrew/science
brew install imagemagick
sudo pip install imageio
brew install opencv
sudo pip install opencv-python
sudo pip install moviepy
sudo pip install BeautifulSoup
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl