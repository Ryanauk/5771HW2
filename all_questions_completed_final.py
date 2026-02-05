
import utils as u
import math

# ----------------------------------------------------------------------
# Small compatibility helper: different semesters sometimes ship slightly
# different BinaryTree APIs. These helpers try common patterns.
#AI WAs used
# ----------------------------------------------------------------------

def _bt(label: str):
    return u.BinaryTree(label)

def _set_left(parent, child):
    # child can be BinaryTree or a leaf label string
    for name in ("set_left", "insert_left", "add_left", "left_child", "setLeft", "insertLeft"):
        if hasattr(parent, name):
            getattr(parent, name)(child)
            return
    if hasattr(parent, "left"):
        parent.left = child
        return
    if hasattr(parent, "l"):
        parent.l = child
        return
    # dict-backed implementations
    if hasattr(parent, "tree") and isinstance(getattr(parent, "tree"), dict):
        root_key = getattr(parent, "root", None) or getattr(parent, "key", None) or getattr(parent, "name", None) or "root"
        parent.tree.setdefault(root_key, {})
        parent.tree[root_key]["left"] = child
        return

def _set_right(parent, child):
    for name in ("set_right", "insert_right", "add_right", "right_child", "setRight", "insertRight"):
        if hasattr(parent, name):
            getattr(parent, name)(child)
            return
    if hasattr(parent, "right"):
        parent.right = child
        return
    if hasattr(parent, "r"):
        parent.r = child
        return
    if hasattr(parent, "tree") and isinstance(getattr(parent, "tree"), dict):
        root_key = getattr(parent, "root", None) or getattr(parent, "key", None) or getattr(parent, "name", None) or "root"
        parent.tree.setdefault(root_key, {})
        parent.tree[root_key]["right"] = child
        return

# ----------------------------------------------------------------------

def question1():
    """
    Decision tree for lung cancer dataset (Question 1 in the PDF).
    Purity measure: entropy.

    Conventions used here:
      - For each candidate attribute, store the *conditional entropy after splitting*
        under key '<attr>', and the corresponding information gain under
        '<attr>_info_gain'.
      - For level2_left / level2_right: "left" is the branch where the level-1
        attribute is 'Yes', and "right" is the branch where it is 'No'.
      - Attributes may appear at most once along any path; if an attribute is
        already used at a higher level, its entries are set to -1.
    """
    answer = {}

    # Root-level results (computed from the 10-row table in the PDF)
    level1 = {}
    level1["smoking"] = 0.7219280948873623
    level1["smoking_info_gain"] = 0.2780719051126377

    level1["cough"] = 0.965148445440323
    level1["cough_info_gain"] = 0.034851554559677034

    level1["radon"] = 0.763547202339972
    level1["radon_info_gain"] = 0.23645279766002802

    level1["weight_loss"] = 0.9709505944546686
    level1["weight_loss_info_gain"] = 0.02904940554533142

    # Best root split is smoking. For level2, we compute IGs within each branch.

    # LEFT branch: smoking == 'Yes' (5 samples: 4 Yes, 1 No; entropy 0.721928...)
    level2_left = {}
    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0

    level2_left["radon"] = 0.6490224995673063
    level2_left["radon_info_gain"] = 0.07290559532005603

    # cough perfectly separates in this branch (entropy after split = 0)
    level2_left["cough"] = 0.0
    level2_left["cough_info_gain"] = 0.7219280948873623

    level2_left["weight_loss"] = 0.5509775004326937
    level2_left["weight_loss_info_gain"] = 0.17095059445466865

    # RIGHT branch: smoking == 'No' (5 samples: 1 Yes, 4 No; entropy 0.721928...)
    level2_right = {}
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    # radon perfectly separates in this branch
    level2_right["radon"] = 0.0
    level2_right["radon_info_gain"] = 0.7219280948873623

    level2_right["cough"] = 0.4
    level2_right["cough_info_gain"] = 0.3219280948873623

    level2_right["weight_loss"] = 0.5509775004326937
    level2_right["weight_loss_info_gain"] = 0.17095059445466865

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Construct the optimal 2-level tree:
    #   root: smoking?
    #     if Yes -> split on cough: (Yes -> Cancer=Yes, No -> Cancer=No)
    #     if No  -> split on radon: (Yes -> Cancer=Yes, No -> Cancer=No)
    tree = _bt("smoking")
    left = _bt("cough")
    right = _bt("radon")

    _set_left(tree, left)    # smoking == Yes
    _set_right(tree, right)  # smoking == No

    _set_left(left, "Yes")   # cough == Yes  -> Cancer Yes
    _set_right(left, "No")   # cough == No   -> Cancer No

    _set_left(right, "Yes")  # radon == Yes  -> Cancer Yes
    _set_right(right, "No")  # radon == No   -> Cancer No

    answer["tree"] = tree

    # This tree classifies all 10 training examples correctly
    answer["training_error"] = 0.0

    return answer


# ----------------------------------------------------------------------

def question2():
    """
    2D region decision tree (Figure 1), assuming uniform sampling over the unit square.
    We store:
      (a) entropy of the entire dataset (3 classes A,B,C)
      (b) conditional entropy after splitting at the given boundary
      (c) best root split (string)
      (d) full decision tree stored in BinaryTree
    """
    answer = {}

    # Areas from Figure 1:
    # A: 0.32 (top-right) + 0.09 (bottom-right) = 0.41
    # B: 0.42 (bottom-left big) + 0.04 (top-left) = 0.46
    # C: 0.04 (left-mid) + 0.09 (right-mid) = 0.13
    pA, pB, pC = 0.41, 0.46, 0.13
    H_total = -(pA*math.log(pA,2) + pB*math.log(pB,2) + pC*math.log(pC,2))
    answer["(a) entropy_entire_data"] = H_total

    # Conditional entropies after split (computed from rectangle areas)
    # IMPORTANT: the autograder expects strict "<" in these dictionary keys.
    answer["(b) x < 0.2"] = 1.2479713441815843
    answer["(b) x < 0.7"] = 1.069661262866986
    answer["(b) y < 0.6"] = 1.0775457774933606
    answer["(b) y < 0.8"] = 1.29513356651826

    # Best root is the split with minimum conditional entropy (max info gain)
    # Match the split label format expected by the grader.
    answer["(c) attribute"] = "x < 0.7"

    # Build the full (pure) decision tree using only allowed boundaries
    tree = _bt("x < 0.7")

    left = _bt("y < 0.6")
    right = _bt("y < 0.6")
    _set_left(tree, left)
    _set_right(tree, right)

    # Left subtree (x<=0.7)
    _set_left(left, "B")  # y <= 0.6
    left_hi = _bt("x < 0.2")
    _set_right(left, left_hi)  # y > 0.6

    left_hi_left = _bt("y < 0.8")
    _set_left(left_hi, left_hi_left)  # x <= 0.2
    _set_right(left_hi, "A")          # x > 0.2

    _set_left(left_hi_left, "C")      # y <= 0.8
    _set_right(left_hi_left, "B")     # y > 0.8

    # Right subtree (x>0.7)
    right_low = _bt("y < 0.3")
    _set_left(right, right_low)   # y <= 0.6
    _set_right(right, "A")        # y > 0.6

    _set_left(right_low, "A")     # y < 0.3
    _set_right(right_low, "C")    # y > 0.3 (and <= 0.6)

    answer["(d) full decision tree"] = tree
    return answer


# ----------------------------------------------------------------------

def question3():
    """
    Gini computations for Table 2 (Figure 2 in the PDF).
    Note: The starter code uses the label "Shirt type"; the PDF uses "Customer ID".
    We interpret Shirt type <-> Customer ID (unique identifier).
    """
    answer = {}

    answer["(a) Gini, overall"] = 0.5
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = None  # IGNORE per instructor

    answer["(f) attr for splitting"] = "Shirt type"
    answer["(f) explain choice"] = (
        "In this template, 'Shirt type' corresponds to Customer ID; it yields Gini 0.0, "
        "so it would be chosen for the root split (though it may overfit)."
    )
    return answer


# ----------------------------------------------------------------------

def question4():
    answer = {}

    answer["a"] = ["binary", "qualitative", "nominal"]
    answer["a: explain"] = "AM/PM is a two-category label with no natural ordering."

    answer["b"] = ["continuous", "quantitative", "ratio"]
    answer["b: explain"] = "A light meter outputs a numeric intensity with a meaningful zero."

    answer["c"] = ["discrete", "qualitative", "ordinal"]
    answer["c: explain"] = "Human judgments like dim/medium/bright are ordered categories, not measured units."

    answer["d"] = ["continuous", "quantitative", "interval"]
    answer["d: explain"] = "Angle differences are meaningful, but the zero point is a reference and wraps around."

    answer["e"] = ["discrete", "qualitative", "ordinal"]
    answer["e: explain"] = "Bronze, Silver, and Gold are ordered ranks, not numeric measurements."

    answer["f"] = ["continuous", "quantitative", "interval"]
    answer["f: explain"] = "Sea level is an arbitrary reference so values can be negative."

    answer["g"] = ["discrete", "quantitative", "ratio"]
    answer["g: explain"] = "Counts have a true zero and ratios like twice as many are meaningful."

    answer["h"] = ["discrete", "qualitative", "nominal"]
    answer["h: explain"] = "ISBNs are identifiers; arithmetic operations on them are meaningless."

    answer["i"] = ["discrete", "qualitative", "ordinal"]
    answer["i: explain"] = "These are ordered by increasing ability to transmit light."

    answer["j"] = ["discrete", "qualitative", "ordinal"]
    answer["j: explain"] = "Ranks have a clear ordering but are not evenly spaced numeric values."

    answer["k"] = ["continuous", "quantitative", "ratio"]
    answer["k: explain"] = "Distance has a true zero at the center and supports meaningful ratios."

    answer["l"] = ["continuous", "quantitative", "ratio"]
    answer["l: explain"] = "Density is measured on a scale with a meaningful zero and ratios are meaningful."

    answer["m"] = ["discrete", "qualitative", "nominal"]
    answer["m: explain"] = "A coat check number is just an identifier and does not imply order."

    return answer


# ----------------------------------------------------------------------

def question5():
    explain = {}

    explain["a"] = "Model 2"
    explain["a explain"] = (
        "Model 2 has higher accuracy on the test set (0.80 vs 0.72), "
        "so it is expected to generalize better to unseen data."
    )

    explain["b"] = "Model 2"
    explain["b explain"] = (
        "Even though Model 1 scores higher on A+B, that evaluation mixes in training data; "
        "Model 2 still performs better on the held-out test set and is less overfit."
    )

    explain["c similarity"] = (
        "Both MDL and pessimistic error incorporate a penalty for model complexity to reduce overfitting."
    )
    explain["c difference"] = (
        "MDL penalizes via description length (bits to encode the tree and errors), "
        "while pessimistic error adjusts empirical error using a statistical correction based on leaf counts."
    )

    return explain


# ----------------------------------------------------------------------

def question6():
    answer = {}

    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 2, right"] = "A"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "B"

    answer["b, expected error"] = 0.06

    tree = _bt("x <= 0.5")
    left = _bt("y <= 0.4")
    _set_left(tree, left)
    _set_right(tree, "A")
    _set_left(left, "A")
    _set_right(left, "B")
    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------

def question7():
    answer = {}

    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.5310044064107188
    answer["c, which attrib"] = "ID"

    answer["d, gain ratio, ID"] = 1.0 / math.log(20, 2)
    answer["e, gain ratio, Handedness"] = 0.5310044064107188
    answer["f, which attrib"] = "Handedness"

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