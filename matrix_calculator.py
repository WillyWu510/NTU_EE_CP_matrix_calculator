class Matrix:
    """The class that describes a descent matrix equipped with some basic functions"""
    
    def __init__(self,row=1,column=1,entry=[0]):
        """Initialize the matrix"""
        
        self.row=row
        self.column=column
        self.entry=entry
        
    def __int__(self):
        """Make all the entries integer."""
        for i in range(self.row):
            for j in range(self.column):
                self.entry[i][j]=int(self.entry[i][j])
                
    def __str__(self):
        """Make all the entries string."""
        for i in range(self.row):
            for j in range(self.column):
                self.entry[i][j]=str(self.entry[i][j])
                
    def __float__(self):
        """Make all the entries float."""
        for i in range(self.row):
            for j in range(self.column):
                self.entry[i][j]=float(self.entry[i][j])
                
    def __round__(self,num):
        """Round all entries to a given precision in decimal digits."""
        for i in range(self.row):
            for j in range(self.column):
                self.entry[i][j]=round(self.entry[i][j],num)
                
    def show(self):
        """Show the matrix row by row."""
        
        for i in range(self.row):
            print(self.entry[i])
            
    def __add__(self,other):
        """Addition of two matrices having the same number of rows and column."""
        
        if self.row!= other.row or self.column!=other.column:
            print("Cannot add.")
        else:
            entries_Sum=[]
            for i in range(self.row):
                entries=[]
                for j in range(self.column):
                    entries.append(self.entry[i][j]+other.entry[i][j])
                entries_Sum.append(entries)
            return Matrix(self.row,self.column,entries_Sum)
        
    def __sub__(self,other):
        """Substraction of two matrices having the same number of rows and column."""
        
        if self.row!= other.row or self.column!=other.column:
            print("Cannot substract.")
        else:
            entries_Dif=[]
            for i in range(self.row):
                entries=[]
                for j in range(self.column):
                    entries.append(self.entry[i][j]+other.entry[i][j])
                entries_Dif.append(entries)
            return Matrix(self.row,self.column,entries_Dif)
        
    def __mul__(self,other):
        """Multiplication of an m*n and an n*p matrices."""
        
        if self.column!=other.row:
            print("Cannot multiply.")
        else:
            entries_Prod=[]
            for i in range(self.row):
                entries=[]
                for j in range(other.column):
                    total=0
                    for k in range(other.row):
                        total+=self.entry[i][k]*other.entry[k][j]
                    entries.append(total)
                entries_Prod.append(entries)
            return Matrix(self.row,other.column,entries_Prod)
    def __eq__(self,other):
        """Two matrices are the same if and only if their entries are the same."""
        return self.entry==other.entry
    
def det(M):
    """Compute the determinant of the matrix"""
    if M.row!=M.column:
        print("Not a square matrix, Can't compute determinant.")
    else:
        total=0
        if M.row==1:
            return M.entry[0][0]
        elif M.row==2:
            return M.entry[0][0]*M.entry[1][1]-M.entry[1][0]*M.entry[0][1] 
        else:
            for j in range(M.column):
                temp_entry=[M.entry[k].copy() for k in range(M.row) if k!=1]
                for k in range(M.row-1):
                    temp_entry[k].pop(j)
                total+=((-1)**(1+j))*M.entry[1][j]*det(Matrix(M.row-1,M.column-1,temp_entry))
            return total

def Transpose(M):
    """The transpose of the given matrix """
    entry_T=[]
    for i in range(M.column):
        entry=[]
        for j in range(M.row):
            entry.append(M.entry[j][i])
        entry_T.append(entry)
    return Matrix(M.column,M.row,entry_T)
        

A=Matrix(3,3,[[1,0,0],[0,3,0],[0,0,5]])
C=Matrix(2,2,[[1,0],[0,3]])
B=Matrix(3,4,[[1,0,0,5],[0,3,0,5],[0,0,5,8]])
D=Matrix(5,5,[[1,0,0,0,0],[0,3,0,0,0],[0,0,5,0,0],[1,0,1,0,1],[0,0,0,0,1]])
(Transpose(B)).show()
(A*B).show()
