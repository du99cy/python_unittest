#check whether list of list is matrix or not
def isRectangularMatrix(list_of_list):
    """_summary_

    Args:
        list_of_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    try:
        columns = len(list_of_list[0])
    except TypeError as exp:
        return False
#if all of sublist in list have the same length then return true
    return all( len(raw)==columns
    for raw in list_of_list )

#create my own matrix that inheritance from list class
class matrix(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def __init__(self,matrix):
        if isRectangularMatrix(matrix):
            super().__init__(matrix)
        else:
            raise ValueError("Given matrices are not the same size.")
            """try:
                raise MatrixSyntaxError('given matrix is list,maxtrix must list of list like [ [ ] ] or given is not matrix')
            except MatrixSyntaxError as exp:
                print(repr(exp))
                raise"""
    def DimensionEqualTo(self,anotherMatrix):
        m = matrix(anotherMatrix)
        return all((len(self)==len(m),len(self[0])==len(m[0])))
    
#check whether all of matrix have the same dimension or not
def isTheSameDimension(matrixes):
    first_matrix = matrix(matrixes[0])
    len_matrix = len(matrixes)
    return all( first_matrix.DimensionEqualTo(matrix) for matrix in matrixes )

def add(*matrixes):#number of List to add
    if isTheSameDimension(matrixes):
        result = [ [0 for col  in raw ] for raw in matrixes[0]]
        x = len(result)
        y= len(result[0])
        lengthLi=len(matrixes)
        for i in range(x):
            for j in range(y):
                for k in range(lengthLi):
                    result[i][j]+=matrixes[k][i][j]
        return result
    else:
        raise ValueError("Given matrices are not the same size.")
        return None