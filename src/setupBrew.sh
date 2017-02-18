ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install ffmpeg
brew link ffmpeg
brew tap homebrew/science
brew install imagemagick
brew install opencv
export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
