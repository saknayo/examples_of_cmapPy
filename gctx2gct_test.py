
from cmapPy.pandasGEXpress import parse_gctx, write_gct

if __name__ == "__main__":
	source_gctx=raw_input("source gctx file path:")
	out_name=raw_input("gct file path:")

	# if you want to parse .gct files ,please import parse_gct.
	in_gctoo=parse_gctx.parse(source_gctx,convert_neg_666=False)

	# the default data_float_format value may result to TypeError,the pandas can't parse it
	write_gct.write(in_gctoo, out_name,data_float_format=None)
	

