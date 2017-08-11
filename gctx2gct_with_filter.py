from cmapPy.pandasGEXpress import parse_gctx, write_gctx, write_gct, parse
import pandas as pd

if __name__ == "__main__":

	#source_gctx=input("source gctx file path:")
	#out_name=input("gct file path:")
	#
	source_gctx="ABC.gctx"
	out_file   ="ABC.gct"
	desc_file  ="inst_info.txt"


	desc_info = pd.read_csv(desc_file, sep="\t")


	# get all samples from Brain
	# about the filter:
	#		the code bellow sellects "id"s of which the "tissue" values contains "Brain" from desc_info
	#	
	# about the "id" : 
	# 		You can run the code below to find the samples of columns.
	#		Then try to find them in inst_info.txt or sig_info.txt, 
	#		the columns title should be the "id"
	# 	
	#       	brain_only_gctoo = parse(source_gctx)
	#       	print(brain_only_gctoo.col_metadata_df[0:5])
	#
	# about the contains method:
	#		It's the method of pandas's Series class.
	#		For detail please view the site below.
	#			https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.contains.html

	brain_ids = desc_info["id"][desc_info["tissue"].str.contains("Brain")  ]

	# how many samples are there in this data set?
	print("number of samples from brain:{}".format(len(brain_ids)))

	#brain_only_gctoo = parse(source_gctx)
	brain_only_gctoo = parse(source_gctx, cid=brain_ids)
	write_gct.write(brain_only_gctoo, out_file ,data_float_format=None)

