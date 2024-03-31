# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Rule 1 only states that if Home Owner = Yes, then DB = Yes. This is not mutually exclusive from the rest of the rules because a person can be a homeowner but also apply to rules 2-5 which don't specify homeownership."
    answers["(b) explain"] = "The rule set doesn't contain every single possible combination of attributes. For example, there is no rule that includes a marital status of Divorced."
    answers["(c) explain"] = "The rule set needs ordering because of rules being covered by other rules (overlapping). For example, if someone is a homeowner, then by rule 1 DB = Yes. However, that same person can also be classified as DB = No if they approach rule 5 first which doesn't ask about homeownership."
    answers["(d) explain"] = "If someone was divorced, not a homeowner, had high annual income, and was currently employed, they wouldn't receive a class. Therefore, a default class would ensure every person got a class if they weren't represented by the rules."

    return answers


# -----------------------------------------------------------
# def question2():

#     ## I WAS TOLD TO SKIP THIS QUESTION ##

#     answers = {}

#     # string "yes" or "no"
#     answers["(a)"] = None
#     answers["(b)"] = None
#     answers["(c)"] = None
#     answers["(d)"] = None

#     # explain_string: explanation in english prose
#     answers["(a) explain"] = None
#     answers["(b) explain"] = None
#     answers["(c) explain"] = None
#     answers["(d) explain"] = None

#     return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "The entry given by pigeon can be classified as Birds by rule 1 and Mammals by rule 3."
    answers["(b) example"] = "Salamanders can not be classified with this rule set because its attributes aren't captured by any rule. It is not Aerial or Aquatic, not warm-blooded, and doesn't give the value No for aquatic creature. Therefore it is left unclassified and the rules are not exhaustive."
    answers["(c) example"] = "If rule 1 came before 3, pigeon would be classified as a bird. However, if rule 3 came before rule 1, pigeon would be classified as a mammal. Therefore, ordering is needed."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = False
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = True

    # explain_string: explanation in english prose
    answers["(a) explain"] = "In back-propigation, the weights are updated backwards. Therefore, the weights at the kth layer are computed using the weights from the k+1th layer, not the other way around as the question asks."
    answers["(b) explain"] = "During testing, forward-propigation occurs and the activations at a layer are computed using the previous layers."
    answers["(c) explain"] = "The vanishing gradient problem occurs when the gradients of the loss function vanish to zero during back-propigation."
    answers["(d) explain"] = "If the model perfectly classifies all training instances and our loss function was one pertaining to accuracy of classifications, then our loss would be zero and thus there wouldn't be any way to improve our loss, thus our gradient of loss would be zero."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 65/100
    answers["(a) P(X_2=1)"] = 41/100
    answers["(a) P(X_1=1,X_2=1)"] = 28/100

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = 'dependent'

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = 'yes'

    # float
    answers["(c) P(X_1=1 | +)"] = 40/50
    answers["(c) P(X_1=1 | -)"] = 25/50
    answers["(c) P(X_2=1 | +)"] = 25/50
    answers["(c) P(X_2=1 | -)"] = 16/50
    answers["(c) P(X_3=1 | +)"] = 20/50
    answers["(c) P(X_3=1 | -)"] = 8/50

    # For each row give the class predicted by the model after training using Naive Bayes

    # here Row 1 corresponds to X_1 = 1, X_2 = 1 , X_3 = 1

    #  Row 2 corresponds to X_1 = 1, X_2 = 0 , X_3 = 0 and similarly Row 3 and Row 4 as well
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '+'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.35

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Our classes are very well separated from eachother. Therefore, we should classify a new data point with the cluster it is closest to."
    answers["(b) explain"] = "Our classes are not very well separated but have high densities for the most part. Therefore, we should use a k value of 5 due to there only being a few instances of classes being amongst a high density of a competing class."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    A=5
    B=4
    C=5
    pos=5
    neg=5

    # float
    answers["(a) P(A=1|+)"] = 3/5
    answers["(a) P(B=1|+)"] = 2/5
    answers["(a) P(C=1|+)"] = 4/5
    answers["(a) P(A=1|-)"] = 2/5
    answers["(a) P(B=1|-)"] = 2/5
    answers["(a) P(C=1|-)"] = 1/5

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "There are 5 instances that result in a positive class. Of those 5 instances, A=1 3 of those times. Therefore, P(A=1|+)=3/5."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    #(3/5)*(2/5)*(4/5)=.192
    #(2/5)*(2/5)*(1/5)=.032
    #(.192)*(.5)/(5/10)*(4/10)*(5/10) = .96
    #(.032)*(.5)/(5/10)*(4/10)*(5/10) = .16
    answers["(b) P(+|R)"] = .96  # WRONG
    answers["(b) P(R|+)"] = .192
    answers["(b) P(R|-)"] = .032

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = 'The probability of the class being positive given R is higher than the probability of the class being -.'
  
    # float
    answers["(c) P(A=1)"] = 5/10
    answers["(c) P(B=1)"] = 4/10
    answers["(c) P(A=1,B=1)"] = 2/10

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 5/10
    answers["(d) P(B=0)"] = 6/10
    answers["(d) P(A=1,B=0)"] = 3/10

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 1/5
    answers["(e) P(A=1|+)"] = 3/5
    answers["(e) P(B=1|+)"] = 2/5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  'P(A=1|+)*P(B=1|+) does not equal P(A=1,B=1|+). Therefore, they are not independent given class +.'
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
