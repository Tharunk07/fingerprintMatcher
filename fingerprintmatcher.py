import cv2
import numpy as np
import os



class fingerprintMatcher:
    """
    A class to perform fingerprint matching.

    Attributes:
    None
    """

    def match_fingerprints(self,img1_path, img2_path):
        """
        Matches two fingerprint images and checks if they are similar.

        Parameters:
        img1_path (str): The file path of the first fingerprint image.
        img2_path (str): The file path of the second fingerprint image.

        Returns:
        None
        """
        test_original = cv2.imread(img1_path)
        fingerprint_database_image = cv2.imread(img2_path)
        
        sift = cv2.xfeatures2d.SIFT_create()

        keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

        matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict()).knnMatch(descriptors_1, descriptors_2, k=2)

        match_points = []
        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                match_points.append(p)

        keypoints_count = min(len(keypoints_1), len(keypoints_2))
        match_ratio = len(match_points) / keypoints_count

        if match_ratio > 0.95:
            print(f"The two images are matched")
            print("percentage(%) of match: ", len(match_points) / keypoints_count * 100)
            result = cv2.drawMatches(test_original, keypoints_1, fingerprint_database_image, keypoints_2, match_points, None)
        else:
            print("Sorry, the fingerprints do not match.")



    def match_with_database(self,test_image_path, database_folder):
        """
        Matches a fingerprint image with a database of fingerprint images.

        Parameters:
        test_image_path (str): The file path of the fingerprint image to match.
        database_folder (str): The folder containing the database of fingerprint images.

        Returns:
        None
        """
        test_original = cv2.imread(test_image_path)
    
        match_found = False
        
        for file in os.listdir(database_folder):
            fingerprint_database_image = cv2.imread(os.path.join(database_folder, file))
           
            sift = cv2.xfeatures2d.SIFT_create()
            
            keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

            matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict()).knnMatch(descriptors_1, descriptors_2, k=2)

            match_points = []
            for p, q in matches:
                if p.distance < 0.1 * q.distance:
                    match_points.append(p)

            keypoints_count = min(len(keypoints_1), len(keypoints_2))
            match_ratio = len(match_points) / keypoints_count

            if match_ratio > 0.95:
                print(f"The image is matched with {file}")
                print("percentage(%) of match: ", len(match_points) / keypoints_count * 100)
                result = cv2.drawMatches(test_original, keypoints_1, fingerprint_database_image, keypoints_2, match_points, None)
                result = cv2.resize(result, None, fx=1, fy=1)
                cv2.imshow("result", result)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()
                match_found = True
                break
        
        if not match_found:
            print("Sorry, your fingerprint is not matched")



