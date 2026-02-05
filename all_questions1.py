# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = {}

    # answer['level1'] is a dict[str,float].

    # Below is a break down showing one way to get the answer. Replace
    # `None` with the correct values.

    level1 = {}

    # Use entropy as the purity measure
    level1["smoking"] = None
    level1["smoking_info_gain"] = None

    level1["cough"] = None
    level1["cough_info_gain"] = None

    level1["radon"] = None
    level1["radon_info_gain"] = None

    level1["weight_loss"] = None
    level1["weight_loss_info_gain"] = None


    # Apply the same approach to fill the elements of `level2_left`

    level2_left = {}

    level2_left["smoking"] = None
    level2_left["smoking_info_gain"] = None

    level2_left["radon"] = None
    level2_left["radon_info_gain"] = None

    level2_left["cough"] = None
    level2_left["cough_info_gain"] = None

    level2_left["weight_loss"] = None
    level2_left["weight_loss_info_gain"] = None


    level2_right = {}

    level2_right["smoking"] = None
    level2_right["smoking_info_gain"] = None

    level2_right["radon"] = None
    level2_right["radon_info_gain"] = None

    level2_right["cough"] = None
    level2_right["cough_info_gain"] = None

    level2_right["weight_loss"] = None
    level2_right["weight_loss_info_gain"] = None


    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right


    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    # Use the class BinaryTree to store the tree.
    # Follow a similar to that found in the
    #    function util.construct_binary_tree

    tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure

    # The training error is defined as the fraction of false
    #   decisions by the tree
    answer["training_error"] = None

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = None
    # Infogain
    answer["(b) x <= 0.2"] = None
    answer["(b) x <= 0.7"] = None
    answer["(b) y <= 0.6"] = None
    answer["(b) y <= 0.8"] = None

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    # Answers are strings
    answer["(c) attribute"] = None


    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    # Use the class BinaryTree to store the tree.
    # Follow a similar to that found in the
    #    function util.construct_binary_tree

    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # type: float
    answer["(a) Gini, overall"] = None

    # type: float
    answer["(b) Gini, ID"] = None
    answer["(c) Gini, Gender"] = None
    answer["(d) Gini, Car type"] = None
    answer["(e) Gini, Shirt type"] = None

    # type: str (one of "Gender", "Car type", "Shirt type")
    answer["(f) attr for splitting"] = None

    # Explanatory text string. At least six words.
    answer["(f) explain choice"] = None

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # Type: a list of three strings:
    #   - Binary, discrete, or continuous
    #   - quantitative or qualitative
    #   - interval or ratio
    #  If you have a choice between 'binary' and 'discrete', choose 'binary'
    #  Always choose the "most" appropriate answer.

    # Explain if there is more than one interpretation. Repeat for the
    #    other questions. At least six words that form a sentence.

    answer["a: explain"] = None
    answer["a"] = None


    answer["b"] = None
    answer["b: explain"] = None

    answer["c"] = None
    answer["c: explain"] = None

    answer["d"] = None
    answer["d: explain"] = None

    answer["e"] = None
    answer["e: explain"] = None

    answer["f"] = None
    answer["f: explain"] = None

    answer["g"] = None
    answer["g: explain"] = None

    answer["h"] = None
    answer["h: explain"] = None

    answer["i"] = None
    answer["i: explain"] = None

    answer["j"] = None
    answer["j: explain"] = None

    answer["k"] = None
    answer["k: explain"] = None

    answer["l"] = None
    answer["l: explain"] = None

    answer["m"] = None
    answer["m: explain"] = None

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = None
    explain["a explain"] = None

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = None
    explain["b explain"] = None

    # A string of at least 10 words.
    explain["c similarity"] = None
    explain["c difference"] = None

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf node.
    answer["a, level 1"] = None
    answer["a, level 2, right"] =None
    answer["a, level 2, left"] = None
    answer["a, level 3, left"] = None
    answer["a, level 3, right"] = None

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = None

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # Type: float
    answer["a, info gain, ID"] = None
    answer["b, info gain, Handedness"] = None

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = None

    # answer is a float
    answer["d, gain ratio, ID"] = None
    answer["e, gain ratio, Handedness"] = None

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = None

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)
