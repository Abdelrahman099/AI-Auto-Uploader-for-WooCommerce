import os 
import shutil  # For moving files
import selenum as sen
import Media as med
import AutoGenProducts as Agp

# Get the path of the images to upload
url = input("Write the path of the pictures you want to upload: ")

# Iterate through the files in the specified directory
for img in os.listdir(url):
    ProductName = " "
    
    # Check if the file is an image by its extension
    if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        
        # Get the product value from the image name
        if img.lower().endswith('.jpeg'):
            value = img.split()[-1][0:-5]  # For .jpeg extension
        else:
            value = img.split()[-1][0:-4]  # For other image extensions
        
        # Construct the product name from the image file name
        for name in img.split()[0:-1]:
            ProductName += name + " "
        
        # Get the full path to the image file
        imgurl = os.path.join(url, img)
        
        # Get the description and short description using selenum
        description, shortdescription = sen.selenum(ProductName)
        
        # Upload the image and get the image ID using the Media module
        ImgId = med.Media(imgurl, ProductName)
        
        # Automatically generate the product information
        Agp.AutoGenPro(ProductName, value, description, shortdescription, ImgId)
        
        # Create the 'Done' folder if it doesn't exist
        done_folder = os.path.join(url, "Done")
        if not os.path.exists(done_folder):
            os.makedirs(done_folder)
        
        # Move the processed image to the 'Done' folder
        shutil.move(imgurl, os.path.join(done_folder, img))

print("All images processed and moved to 'Done' folder.")
    