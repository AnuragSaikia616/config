#! /bin/sh

echo Enter '0' for Transparent '1' for Gruvbox:
read input

#############################################
#   CREATES BACKUP AT ~/.dotfiles_backup 
backup(){
  echo backup funtion called
rm -rf ~/.dotfiles_backup 
mkdir ~/.dotfiles_backup
cp -r ~/.config/qtile ~/.dotfiles_backup
}
#############################################


case $input in
  0)
    #sets transparent theme
    backup
    cp -r ~/dotfiles_linux/Qtile_config_transparent/* ~/.config/qtile/
    echo set theme transparent

    ;;
  1)
    #sets gruvbox theme
    backup
    cp -r ~/dotfiles_linux/Qtile_config_gruvbox_modified/* ~/.config/qtile/
    echo set theme gruvbox
    ;;
  *)
    echo INVALID
    echo EXITING...
esac
