row1=['1','1','1']
row2=['1','1','1']
row3=['1','1','1']
matrix=[row1,row2,row3]
print(f"{row1}\n {row2}\n {row3}")
position=input("enter position:")
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]='X'
print(f" {row1}\n {row2}\n {row3}")