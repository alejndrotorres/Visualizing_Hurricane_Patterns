"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
1) Name - Alejandro atorres1@sandiego.edu
2) Name - Nachi nelzaurdia@sandiego.edu
"""

def average_review(word, review_filename):
    

    review_file = open(review_filename, 'r')
    count = 0
    total_score = 0
    lowercase_word = word.lower()
    for line in review_file:
        # make lower case to avoid case sensitivity
        lower_line = line.lower()  
        review_words = lower_line.split()
        i = int(review_words[0])
        if lowercase_word in review_words[1:]:
            count = count + 1
            total_score = total_score + i
        
    if count > 0:
        average_score = total_score/(count)
    else:
        average_score = 2.0
    


    # done reading file, so close it
    review_file.close()

    return float(average_score)

    


def estimate_review_score(movie_review, review_filename):
    word_review = 0
    file = movie_review.lower()
    filesplit = file.split()
    count = 0

    for word in filesplit:
        word_review = average_review(word, review_filename)
        count = count+word_review
        avg_review = count/(len(filesplit))

        return avg_review




def estimate_user_review():
    reviewinp = input("Enter a movie review: ")
    reviewfile = input("Enter the name of the review: ")
    reviewcomment = (int(round(estimate_review_score(reviewinp,reviewfile))))
    file = estimate_review_score(reviewinp, reviewfile)
    if reviewcomment == 0:
        comment = ("negative")
    elif reviewcomment == 1:
        comment = ("somewhat negative")
    elif reviewcomment == 2:
        comment = ("neutral")
    elif reviewcomment == 3:
        comment = ("somewhat positive")
    else: 
        comment = ("positive")
    print("estimated score:",file, comment)



if __name__ == "__main__":
    estimate_user_review()
