import cv2
import os 

save_path = 'C:\\Users\\bulzg\\Desktop\\img_reale'
os.chdir(save_path)
lst = os.listdir()
 

for i in lst:
    img = cv2.imread(i, cv2.IMREAD_UNCHANGED)
    
    dim = (224, 224)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite('C:\\Users\\bulzg\\Desktop\\img_reale_resize\\' + i,resized)
    
