with open('tmp', 'w') as f:
  for i in range(30):
    f.write('\\begin{subfigure}[t]{0.19\\textwidth}\n')
    f.write('\\centering\n')
    f.write('\\includegraphics[width=\\textwidth]{./images/marginals_iter_' + str(i + 1) + '.png}\n')
    f.write('\\vspace{-0.6cm}\n')
    f.write('\\caption{iteration=' + str(i + 1) + '}\n')
    f.write('\\end{subfigure}\n')

