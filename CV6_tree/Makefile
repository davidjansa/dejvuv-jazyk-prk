GCC := gcc
GCC_OPT := Wall
ASM_OPT := S

INPUT := hello
ast: clean
	@$(GCC) $(INPUT).c -fdump-tree-original-raw
	pwd
	@./pre.awk  a-$(INPUT).c.005t.original | ./tree_viz.awk > tree.dot
	@dot -Tpng tree.dot -o tree.png

dump: clean
	@$(GCC) $(INPUT).c -fdump-tree-all

clean:
	@rm -rf *.o        #clean all the object files
	@rm -rf $(INPUT)     #clean all the binaries
	@rm -rf $(INPUT).asm    #clean the asm output
	@rm -rf $(INPUT).c.*    #clean all the syntax trees