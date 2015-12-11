# bitrate-eval
Loops through your iTunes library and evaluates bitrates

Default Outputs
- Notes file formats that aren't mp3
- Notes files that are less than 320kbps

Currently this project only barely works. 
- There are issues with the library implemented to evaluate bitrates (ie. not all mp3's @ 320kbps will be evaluated as such)
- For some reason the virtual environment won't always be setup properly

How-to:
- Consult the references file to set your specs, it should run out-of-the-repo if you're on a Mac with iTunes and no complicated setup
- On the command line, run 'bash run.sh'
