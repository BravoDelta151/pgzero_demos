
import os
import pygame

##################################
# Options
##################################
rename_files = True     # remove parens, replace spaces with underscore, make lower
copy_flip = True        # creates a copy of the image and flips it horizontally
print_file_list = True  # prints out the files in the directory
print_full_path = True  # a sub option for print file list, if false only the file name is printed

# suffix for files that are copy_flip'd, added prior to .png in file name
cf_suffix = 'left'

# relative location of images, i.e. current working directory (a.k.a. cwd) then this path
# it is a good practice to put copies in a different folder to make it easier to verify
src_folders = ["images", "Adventure Girl", "orig"]
dest_folders = ["images", "Adventure Girl", "changed"] # src_folders

src_path = '{}'.format(os.sep).join(src_folders)
dest_path = '{}'.format(os.sep).join(dest_folders)

##################################
# HELPER FUNCTIONS
##################################
def get_dir_path(dirname = "", filename=None):
    cwd = os.getcwd()
    if dirname != "":
        dir_path = os.path.join(cwd, dirname)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        if filename:
            return os.path.join(dir_path, filename)
        else:
            return dir_path
    else:
        return cwd

def get_dir_list(dirname = ""):    
    return os.listdir(get_dir_path(dirname))
    

def flip_image(src):
    print('copy_flip image -> ', end= '')
    image = pygame.image.load(src)
    dest = src.replace('.png', '{}.png'.format(cf_suffix))
    #print("Saving: {}".format(dest))
    save_image(pygame.transform.flip(image, True, False), dest)


def save_image(image, full_name):
    print("saving: {}".format(full_name))
    try:
        pygame.image.save(image, full_name)
    except Exception as e:
        print("Save error: {}".format(e.message))


def rename_image(src, dest):
    print('rename image ->  ', end='')
    image = pygame.image.load(src)
    save_image(image, dest)


##################################
# Main process
##################################
def main():
    # get list of files
    dir_list = get_dir_list(src_path)

    # for each item in list
    for item in dir_list:  
        
        # get full path to source
        src = get_dir_path(src_path, item)
        if rename_files:
            f = str(item).replace(' ', '_').replace('(','').replace(')','').strip().lower()
        else:
            f = item
        
        # tf = 'ag_{}'.format(f)
        
        # get full path to destination
        dest = get_dir_path(dest_path, f)
        
        
        # check that it is a file and not a subdirectory        
        if os.path.isfile(src): 
            if print_file_list:
                if print_full_path:
                    print('source: {}'.format(src))
                    print('dest: {}'.format(dest))
                
            else:
                print(item)
                
            if rename_files:
                rename_image(src, dest)
                if copy_flip:
                    flip_image(dest)
            elif copy_flip:
                flip_image(src)            


##################################
# call main()
##################################
if __name__ == '__main__':
    main()