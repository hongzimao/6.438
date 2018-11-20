tw = 0.09
d = 0.001

with open('latex_figures', 'w') as f:
    for i in range(10):
        f.write('%\n')
        f.write('\\begin{subfigure}[t]{' + str(tw) + '\\textwidth}\n')
        f.write('\\centering\n')
        f.write('\\includegraphics[width=\\textwidth]{./computational/results/gibbs_node_sampler_positive_iter_' + str(i * 100) + '.png}\n')
        f.write('\\vspace{-0.6cm}\n')
        # f.write('\\caption{iteration=' + str(max(1, i * 100)) + '}\n')
        f.write('\\end{subfigure}\\hspace{' + str(d) + '\\textwidth}\n')
        f.write('%\n')

    for i in range(10):
        f.write('%\n')
        f.write('\\begin{subfigure}[t]{' + str(tw) + '\\textwidth}\n')
        f.write('\\centering\n')
        f.write('\\includegraphics[width=\\textwidth]{./computational/results/gibbs_node_sampler_negative_iter_' + str(i * 100) + '.png}\n')
        f.write('\\vspace{-0.6cm}\n')
        # f.write('\\caption{iteration=' + str(max(1, i * 100)) + '}\n')
        f.write('\\end{subfigure}\\hspace{' + str(d) + '\\textwidth}\n')
        f.write('%\n')

    for i in range(10):
        f.write('%\n')
        f.write('\\begin{subfigure}[t]{' + str(tw) + '\\textwidth}\n')
        f.write('\\centering\n')
        f.write('\\includegraphics[width=\\textwidth]{./computational/results/gibbs_comb_sampler_positive_iter_' + str(i * 100) + '.png}\n')
        f.write('\\vspace{-0.6cm}\n')
        # f.write('\\caption{iteration=' + str(max(1, i * 100)) + '}\n')
        f.write('\\end{subfigure}\\hspace{' + str(d) + '\\textwidth}\n')
        f.write('%\n')

    for i in range(10):
        f.write('%\n')
        f.write('\\begin{subfigure}[t]{' + str(tw) + '\\textwidth}\n')
        f.write('\\centering\n')
        f.write('\\includegraphics[width=\\textwidth]{./computational/results/gibbs_comb_sampler_negative_iter_' + str(i * 100) + '.png}\n')
        f.write('\\vspace{-0.6cm}\n')
        # f.write('\\caption{iteration=' + str(max(1, i * 100)) + '}\n')
        f.write('\\end{subfigure}\\hspace{' + str(d) + '\\textwidth}\n')       
        f.write('%\n')


