from helpers import *

POSTS = [

car("2026-11-05", "o-que-a-smartcontax-faz", [
    C("Prazer, Smartcontax", "Contabilidade que *ajuda a decidir*, não só a pagar", "Para clínicas e empresas que querem clareza sobre os próprios números.", "4 coisas que entregamos além da guia do mês"),
    S("01", "Imposto *calculado* e conferido", [("O que fazemos", "Apuração mensal, obrigações acessórias e conferência das notas emitidas e recebidas."), ("Por que importa", "Erro de enquadramento não aparece no mês. Aparece na fiscalização, com juros e multa.")]),
    S("02", "Regime tributário *revisado*", [("O que fazemos", "Comparamos Simples, Presumido e Real com os números reais da empresa."), ("Por que importa", "Regime escolhido na abertura e nunca revisto costuma ficar caro quando a empresa cresce.")]),
    S("03", "Números para *decidir*", [("O que fazemos", "Organizamos faturamento, custos e margem de forma que o dono consiga ler."), ("Por que importa", "Contratar, investir ou retirar lucro são decisões que dependem desses números.")]),
    S("04", "Atendimento *onde você está*", [("Como funciona", "Contabilidade 100% digital. Falamos por WhatsApp, videochamada ou vamos até a sua empresa.")], box="Você não precisa ir até um escritório para ter um contador presente."),
    A("Conheça a forma como trabalhamos", "Siga o @smartcontax para receber conteúdo sobre impostos, gestão e Reforma Tributária de segunda a sexta.", "Envie para um sócio ou colega empresário"),
], """
A maioria dos empresários só fala com o contador quando chega a guia para pagar.

A Smartcontax nasceu para mudar essa relação. Além de apurar impostos e cumprir obrigações, revisamos o regime tributário, organizamos os números para que você consiga ler e tomar decisão, e atendemos onde você estiver: WhatsApp, videochamada ou na sua empresa.

Nosso foco são clínicas (odontológicas, médicas e veterinárias) e empresas do comércio que querem crescer com segurança fiscal.

Salve este post e acompanhe o perfil: a partir de hoje, conteúdo novo de segunda a sexta.

#contabilidade #contabilidadeconsultiva #gestaoempresarial #clinicas #smartcontax
"""),

car("2026-11-06", "2027-o-que-muda", [
    C("Reforma Tributária", "Menos de 2 meses para *2027*: o que muda na prática", "A fase de teste acaba. A CBS passa a ser cobrada de verdade.", "5 mudanças que atingem clínicas e comércio"),
    S("01", "PIS e Cofins *deixam de existir*", ["A partir de 2027, a CBS (Contribuição sobre Bens e Serviços) substitui PIS e Cofins.", "Empresas fora do Simples passam a apurar a CBS no lugar dessas duas contribuições."]),
    S("02", "IPI vai a *zero* para quase tudo", ["O IPI tem alíquota zerada a partir de 2027, com exceção dos produtos que têm industrialização incentivada na Zona Franca de Manaus."]),
    S("03", "Chega o *Imposto Seletivo*", ["Incide sobre produtos considerados prejudiciais à saúde ou ao meio ambiente, como cigarros, bebidas alcoólicas e bebidas açucaradas.", "Está previsto para 2027, com alíquotas ainda em definição. Para a maioria das clínicas, o efeito é indireto."]),
    S("04", "IBS ainda em *teste*", ["Em 2027 e 2028 o IBS segue com alíquota reduzida, de transição. ICMS e ISS continuam valendo normalmente até 2028.", "A redução gradual de ICMS e ISS começa em 2029."]),
    S("05", "Notas fiscais *mudam de campo*", ["Os documentos fiscais precisam trazer IBS e CBS corretamente classificados."], box="Se o seu sistema emissor ainda não foi atualizado, isso precisa entrar na lista de dezembro."),
    A("Prepare a empresa antes de janeiro", "A Reforma não muda tudo de uma vez, mas 2027 é o primeiro ano em que ela pesa no caixa.", "Envie para o sócio que cuida das finanças"),
], """
Em 2026 a Reforma Tributária esteve em fase de teste. Em 2027 ela começa a pesar no caixa.

O principal ponto: a CBS substitui PIS e Cofins para empresas fora do Simples Nacional. O IPI é zerado para a maioria dos produtos, o Imposto Seletivo está previsto para começar e o IBS segue com alíquota reduzida, com ICMS e ISS valendo normalmente até 2028. A alíquota de referência da CBS ainda depende de resolução do Senado.

Para clínicas no Lucro Presumido, a troca de PIS e Cofins pela CBS muda o cálculo e a forma de aproveitar créditos. Para o comércio, muda também a nota fiscal.

Salve para revisar em dezembro e compartilhe com quem cuida das finanças da sua empresa.

#reformatributaria #cbs #ibs #lucropresumido #contabilidade
"""),

img("2026-11-07", "cbs-substitui-pis-cofins", {
    "theme": "navy", "kicker": "Reforma Tributária", "big": "2027", "bigsize": 220,
    "title": "PIS e Cofins *saem*. A CBS *entra*.",
    "text": "Para empresas fora do Simples Nacional, a apuração muda a partir de janeiro. Base, créditos e notas fiscais seguem novas regras.",
    "foot": "LC 214/2025",
}, """
2027 é o ano em que a CBS substitui PIS e Cofins.

Na prática, empresas do Lucro Presumido e do Lucro Real passam a apurar um tributo novo, com regras próprias de crédito e de destaque na nota fiscal. Quem está no Simples Nacional continua recolhendo pelo DAS, mas pode ser afetado pela forma como os clientes aproveitam créditos.

Salve este post e acompanhe a série sobre a Reforma no perfil.

#reformatributaria #cbs #pisecofins #contabilidade
"""),

car("2026-11-08", "sinais-regime-errado", [
    C("Gestão tributária", "5 sinais de que sua empresa pode estar no *regime errado*", "Regime tributário não é escolha para a vida toda.", "Se você se identificou com 2 ou mais, vale revisar"),
    S("01", "O faturamento *mudou muito*", ["A empresa abriu com um porte e hoje fatura o dobro ou o triplo.", "As faixas do Simples e as bases do Presumido reagem de forma diferente ao crescimento."]),
    S("02", "A folha *cresceu ou encolheu*", ["Em atividades sujeitas ao Fator R, como odontologia e medicina, a relação entre folha e faturamento muda o anexo do Simples.", "Contratar ou demitir pode mudar o imposto."]),
    S("03", "Ninguém fez *simulação*", ["Se o regime foi escolhido na abertura e nunca mais comparado, a decisão foi tomada com números que não existem mais."]),
    S("04", "A margem *não fecha*", ["Faturamento alto, caixa apertado e nenhuma explicação clara.", "Imposto é um dos primeiros itens a investigar."]),
    S("05", "Você não sabe *quanto paga*", ["Se você não sabe qual percentual do faturamento vai para impostos, não consegue saber se esse número é justo."], box="A entrada no Simples agora tem prazo em setembro. Quem perde a janela só muda no ano seguinte."),
    A("Revise com antecedência", "A escolha do regime vale para o ano inteiro. A análise precisa vir meses antes do prazo, não na véspera.", "Envie para um empresário que precisa revisar"),
], """
Regime tributário escolhido na abertura e nunca revisado é um dos erros mais comuns que encontramos.

A empresa cresce, a folha muda, a margem aperta, e o enquadramento continua o mesmo. Em atividades como odontologia e medicina, o Fator R pode mudar o anexo do Simples. No Presumido, o crescimento muda o adicional de IR.

Desde a LC 214/2025, a opção pelo Simples Nacional é feita em setembro, para valer no ano seguinte. Para o Presumido e o Real, a escolha se confirma no primeiro pagamento do ano. Em qualquer caso, a análise precisa vir antes do prazo.

Salve e compartilhe com quem precisa fazer essa revisão.

#regimetributario #simplesnacional #lucropresumido #planejamentotributario #contabilidade
"""),

car("2026-11-09", "pro-labore-x-lucros", [
    C("Remuneração dos sócios", "Pró-labore ou *distribuição de lucros*?", "As duas formas são legais. O erro está em usar uma no lugar da outra.", "O que diferencia cada uma e quando usar"),
    S("01", "Pró-labore", [("O que é", "A remuneração pelo trabalho do sócio na empresa."), ("O que incide", "INSS de 11% descontado do sócio, até o teto, e Imposto de Renda pela tabela mensal. Fora do Simples, a empresa ainda recolhe 20% de contribuição previdenciária.")]),
    S("02", "Distribuição de lucros", [("O que é", "A divisão do resultado que a empresa gerou."), ("O que incide", "Não tem INSS. Desde 2026, valores acima de R$ 50 mil por mês, pagos pela mesma empresa à mesma pessoa, têm retenção de 10% de IR (Lei 15.270/2025).")]),
    S("03", "O erro *mais comum*", ["Retirar tudo como lucro e não registrar pró-labore.", "Quem trabalha na empresa deve ter pró-labore. Sem ele, há risco de a Receita requalificar os valores e cobrar INSS."]),
    S("04", "O jeito certo", ["Pró-labore compatível com a função e com a realidade da empresa.", "Lucro distribuído com base na contabilidade, depois de apurado."], box="Sem escrituração contábil, a distribuição isenta fica limitada à base presumida, descontados os impostos."),
    A("Retirada com regra é retirada segura", "O valor ideal depende do regime, da folha e do lucro apurado. Não existe percentual padrão para todos.", "Envie para o seu sócio"),
], """
Pró-labore e distribuição de lucros não são a mesma coisa, e usar um no lugar do outro gera risco.

Pró-labore remunera o trabalho do sócio e tem INSS e IR. Distribuição de lucros divide o resultado da empresa, sem INSS, mas desde 2026 tem retenção de 10% de IR quando passa de R$ 50 mil por mês para a mesma pessoa, conforme a Lei 15.270/2025.

O erro mais comum é retirar tudo como lucro e não ter pró-labore. Outro é distribuir lucro sem contabilidade que comprove o resultado.

Salve para consultar e envie para o seu sócio.

#prolabore #distribuicaodelucros #socios #gestaofinanceira #contabilidade
"""),

car("2026-11-10", "conta-pf-pj-misturada", [
    C("Erros de gestão", "Conta da empresa e conta pessoal *misturadas*", "Parece prático. Custa caro depois.", "4 riscos e como corrigir"),
    S("01", "Você perde o *controle real*", [("O problema", "Pagamentos pessoais saindo da conta da empresa."), ("O risco", "Ninguém sabe quanto a empresa lucrou de verdade. O caixa parece menor ou maior do que é.")]),
    S("02", "Retirada vira *problema fiscal*", [("O problema", "Dinheiro que sai sem classificação."), ("O risco", "Pode ser tratado como remuneração sem recolhimento de INSS e IR, ou como receita omitida.")]),
    S("03", "A contabilidade *não fecha*", [("O problema", "Extrato com despesas que não são da empresa."), ("O risco", "Balanço sem credibilidade para banco, investidor ou um futuro sócio.")]),
    S("04", "O patrimônio *se confunde*", [("O problema", "Bens e dívidas da pessoa e da empresa no mesmo lugar."), ("O risco", "Em discussões judiciais, a confusão patrimonial pode atingir os bens pessoais do sócio.")], box="O jeito certo: defina um pró-labore, transfira para a conta pessoal e pague as despesas pessoais de lá."),
    A("Separar é o primeiro passo da gestão", "Uma retirada fixa por mês já resolve a maior parte do problema.", "Envie para quem ainda mistura as contas"),
], """
Pagar a conta de casa com o cartão da empresa parece não ter consequência. Tem.

Quando as contas se misturam, você perde a noção do lucro real, a contabilidade deixa de refletir a empresa e as retiradas sem classificação podem virar problema fiscal. Em casos mais graves, a confusão patrimonial pode atingir os bens pessoais do sócio.

A correção é simples: defina um pró-labore, transfira esse valor para a sua conta pessoal e pague suas despesas de lá.

Salve e compartilhe com quem ainda mistura as contas.

#gestaofinanceira #pessoajuridica #fluxodecaixa #empreendedorismo #contabilidade
"""),

img("2026-11-11", "mito-mei-dentista", {
    "theme": "light", "chip": "Mito", "chipbg": "#B3261E",
    "title": "“Dentista pode abrir *MEI* para pagar menos imposto.”",
    "text": "Atividades de profissão regulamentada, como odontologia, medicina e psicologia, não podem ser exercidas como MEI.",
    "box": "Para o profissional de saúde, as opções são outras: pessoa física, Simples Nacional ou Lucro Presumido.",
}, """
Essa dúvida aparece com frequência, e a resposta é não.

O MEI só é permitido para as atividades listadas pelo Comitê Gestor do Simples Nacional, e profissões regulamentadas como odontologia, medicina e psicologia não fazem parte da lista. Abrir MEI com uma atividade diferente para emitir nota de serviço de saúde é irregular.

O caminho correto é comparar atuação como pessoa física, Simples Nacional e Lucro Presumido com base no faturamento real.

Salve e envie para um colega da área da saúde.

#mei #dentista #contabilidadeparadentistas #simplesnacional
"""),

car("2026-11-12", "fator-r", [
    C("Simples Nacional", "Fator R: a conta que muda o *imposto da clínica*", "Entenda em 4 passos por que a folha de pagamento interfere no Simples.", "Vale para odontologia, medicina e outras atividades"),
    S("01", "O que é", ["É a relação entre a folha de pagamento dos últimos 12 meses e a receita bruta do mesmo período.", "A folha inclui salários, pró-labore e encargos como INSS patronal e FGTS."]),
    S("02", "A regra dos *28%*", [("Igual ou acima de 28%", "A atividade é tributada pelo Anexo III, com alíquota inicial de 6%."), ("Abaixo de 28%", "A atividade vai para o Anexo V, com alíquota inicial de 15,5%.")]),
    S("03", "Onde muita gente *erra*", ["Não incluir o pró-labore na folha.", "Não acompanhar mês a mês. O cálculo é móvel e pode mudar de anexo de um mês para o outro."]),
    S("04", "O que fazer", ["Calcular o Fator R todo mês, antes de apurar o DAS.", "Avaliar se um ajuste de pró-labore compensa, considerando também o INSS e o IR que incidem sobre ele."], box="Aumentar o pró-labore só para atingir 28% nem sempre compensa. A conta precisa ser feita caso a caso."),
    A("Fator R é cálculo mensal", "Se ninguém confere esse número na sua empresa, comece por aqui.", "Envie para o sócio que cuida das finanças"),
], """
Duas clínicas com o mesmo faturamento podem pagar alíquotas muito diferentes no Simples Nacional. A explicação, muitas vezes, é o Fator R.

Ele compara a folha de pagamento dos últimos 12 meses, incluindo pró-labore e encargos, com a receita bruta do mesmo período. Igual ou acima de 28%, a atividade fica no Anexo III, com alíquota inicial de 6%. Abaixo disso, vai para o Anexo V, que começa em 15,5%.

O cálculo muda todo mês. Ajustar o pró-labore pode compensar, mas a conta precisa incluir INSS e IR.

Salve para consultar e compartilhe com quem cuida das finanças da clínica.

#fatorr #simplesnacional #clinicaodontologica #contabilidadeparamedicos #contabilidade
"""),

car("2026-11-13", "equiparacao-hospitalar", [
    C("Lucro Presumido", "Equiparação hospitalar: *redução real* de IR e CSLL", "Um benefício legal que muitas clínicas desconhecem.", "Quem pode usar e quais cuidados tomar"),
    S("01", "Como funciona", ["No Lucro Presumido, serviços em geral têm base de 32% para IRPJ e CSLL.", "Serviços hospitalares e alguns serviços de diagnóstico podem usar base de 8% para IRPJ e 12% para CSLL."]),
    S("02", "Quem *pode* usar", ["Clínicas que prestam serviços de promoção à saúde, como procedimentos, exames e cirurgias, conforme entendimento consolidado no STJ.", "Não é necessário ter internação."]),
    S("03", "As *condições*", ["Ser sociedade empresária, com registro na Junta Comercial.", "Cumprir as normas da Anvisa e ter a estrutura adequada à atividade."]),
    S("04", "O que *não entra*", ["Consultas simples não se enquadram.", "A receita precisa ser segregada entre o que é procedimento e o que é consulta."], box="Benefício mal aplicado gera autuação. Documentação e segregação de receitas são obrigatórias."),
    A("Vale a análise da sua clínica", "O ganho depende do tipo de serviço prestado e da estrutura da empresa.", "Envie para um colega dono de clínica"),
], """
No Lucro Presumido, a maioria dos serviços usa base de 32% para calcular IRPJ e CSLL. Serviços hospitalares podem usar base de 8% para IRPJ e 12% para CSLL. É a chamada equiparação hospitalar.

O STJ já firmou entendimento de que não é preciso ter internação: o que importa é a natureza do serviço. Mas há condições. A clínica precisa ser sociedade empresária, cumprir as normas da Anvisa e segregar as receitas, porque consultas simples não entram no benefício.

Aplicado sem documentação, o benefício vira autuação. Aplicado corretamente, reduz de forma relevante o imposto.

Salve e envie para quem tem clínica no Lucro Presumido.

#equiparacaohospitalar #lucropresumido #clinicas #planejamentotributario #contabilidade
"""),

img("2026-11-14", "checklist-documentos-mes", {
    "theme": "white", "kicker": "Rotina mensal",
    "title": "O que enviar ao contador *todo mês*",
    "text": "• Extratos de todas as contas da empresa\n• Notas fiscais emitidas e recebidas\n• Recibos e comprovantes de despesas\n• Admissões, demissões e alterações na folha\n• Contratos novos ou alterados",
    "box": "Documento que chega atrasado vira imposto calculado com informação incompleta.",
}, """
A qualidade da contabilidade depende da qualidade da informação que chega até ela.

Todo mês, cinco grupos de documentos são essenciais: extratos de todas as contas, notas emitidas e recebidas, comprovantes de despesas, movimentações da folha e contratos novos ou alterados.

Sem isso, o imposto é calculado com informação incompleta e o balanço deixa de representar a empresa.

Salve este checklist e deixe no seu calendário mensal.

#rotinacontabil #gestaoempresarial #contabilidade #organizacaofinanceira
"""),

img("2026-11-15", "frase-imposto-sem-surpresa", {
    "theme": "orange", "kicker": "Nossa visão",
    "title": "Imposto certo não é o *menor* imposto. É o imposto *sem surpresa*.",
    "text": "Planejamento tributário é pagar o que a lei exige, pelo caminho que a lei permite, com previsibilidade para o seu caixa.",
}, """
Planejamento tributário não é truque para pagar menos.

É escolher, dentro da lei, o caminho mais adequado para a sua empresa, e saber com antecedência quanto vai sair do caixa. A surpresa é o que mais custa: multa, juros, guia que ninguém esperava.

Na Smartcontax, trabalhamos com esse princípio.

Compartilhe com quem pensa da mesma forma.

#planejamentotributario #contabilidadeconsultiva #gestaoempresarial
"""),

car("2026-11-16", "13-salario-guia", [
    C("Departamento pessoal", "13º salário: *prazos* e cálculo sem erro", "Duas parcelas, regras diferentes para cada uma.", "Guia rápido para quem tem funcionários"),
    S("01", "Os *prazos*", [("1ª parcela", "Até 30 de novembro."), ("2ª parcela", "Até 20 de dezembro. Em 2026 a data cai em um domingo, então o pagamento deve ser feito até sexta-feira, 18/12.")]),
    S("02", "Como *calcular*", ["O 13º é proporcional: 1/12 do salário para cada mês trabalhado no ano.", "Conta como mês completo aquele em que o funcionário trabalhou 15 dias ou mais."]),
    S("03", "O que *entra* na base", ["Salário e médias de variáveis habituais, como horas extras, comissões e adicionais."]),
    S("04", "Os *descontos*", ["A 1ª parcela corresponde à metade do valor, sem descontos de INSS e IR.", "Os descontos de INSS e IR são feitos na 2ª parcela. O FGTS incide sobre as duas."], box="Separe o valor das duas parcelas e dos encargos no caixa de novembro e dezembro."),
    A("Dezembro pesa no caixa", "13º, férias e encargos se concentram no fim do ano. Planejar agora evita aperto.", "Envie para quem cuida da folha"),
], """
O 13º salário tem duas datas: 1ª parcela até 30 de novembro e 2ª parcela até 20 de dezembro. Como 20/12/2026 cai em um domingo, a 2ª parcela deve ser paga até sexta-feira, 18/12.

O valor é proporcional aos meses trabalhados, considerando como mês completo o período de 15 dias ou mais. Médias de horas extras, comissões e adicionais habituais entram na base.

A 1ª parcela é metade do valor, sem descontos. INSS e IR são descontados na 2ª. O FGTS incide nas duas.

Salve para consultar e envie para quem cuida da folha.

#13salario #departamentopessoal #folhadepagamento #gestaodepessoas #contabilidade
"""),

car("2026-11-17", "dividendos-2026", [
    C("Lei 15.270/2025", "Distribuição de lucros *mudou em 2026*", "O lucro continua sem INSS, mas o Imposto de Renda passou a ter novas regras.", "O que todo sócio precisa saber"),
    S("01", "Retenção de *10%*", ["Lucros pagos pela mesma empresa à mesma pessoa física acima de R$ 50 mil no mês têm retenção de 10% de IR na fonte.", "Abaixo desse valor mensal, não há retenção."]),
    S("02", "Imposto *mínimo anual*", ["Pessoas físicas com renda total acima de R$ 600 mil no ano passam a ter uma tributação mínima, que chega a 10% para rendas a partir de R$ 1,2 milhão.", "O imposto já pago entra no cálculo."]),
    S("03", "E o lucro *até 2025*?", ["Lucros apurados até 2025, com distribuição aprovada até 31/12/2025, seguem regras de transição previstas na lei."]),
    S("04", "O que fazer *agora*", ["Rever a política de retiradas dos sócios para 2027.", "Avaliar o equilíbrio entre pró-labore e lucro com números reais."], box="Concentrar retiradas em um único mês pode gerar retenção que seria evitável com planejamento."),
    A("Planeje as retiradas de 2027", "A regra é nova e ainda gera dúvidas. Decisão sem cálculo pode sair cara.", "Envie para o seu sócio"),
], """
Desde 2026, a distribuição de lucros tem regras novas de Imposto de Renda, trazidas pela Lei 15.270/2025.

Lucros pagos pela mesma empresa à mesma pessoa física acima de R$ 50 mil no mês têm retenção de 10% na fonte. Além disso, quem tem renda total acima de R$ 600 mil no ano passa a ter um imposto mínimo anual, considerando o que já foi pago.

O lucro continua sem INSS, mas a forma de retirar passou a importar mais. Concentrar valores em um único mês, por exemplo, pode gerar retenção desnecessária.

Salve e compartilhe com o seu sócio antes de definir as retiradas de 2027.

#distribuicaodelucros #dividendos #impostoderenda #lei15270 #contabilidade
"""),

img("2026-11-18", "alerta-13-primeira", {
    "theme": "navy", "kicker": "Alerta de prazo", "big": "30/11", "bigsize": 230,
    "title": "Último dia para a *1ª parcela* do 13º salário",
    "text": "Corresponde a metade do valor devido, sem descontos de INSS e IR. O FGTS incide sobre o pagamento.",
    "foot": "Lei 4.749/1965",
}, """
Faltam 12 dias para o prazo da 1ª parcela do 13º salário: 30 de novembro.

Ela corresponde a metade do valor proporcional aos meses trabalhados, sem descontos de INSS e IR. O FGTS incide sobre ela. Pagamento fora do prazo pode gerar multa.

Se a folha da sua empresa ainda não está pronta, este é o momento de conferir.

Salve e envie para quem cuida do departamento pessoal.

#13salario #departamentopessoal #prazos #contabilidade
"""),

car("2026-11-19", "custo-hora-clinica", [
    C("Gestão de clínicas", "Quanto custa *uma hora* da sua clínica?", "Sem esse número, o preço do procedimento é um chute.", "Como calcular em 4 passos"),
    S("01", "Some os *custos fixos*", ["Aluguel, folha, pró-labore, sistemas, contabilidade, energia, internet e manutenção.", "Use a média dos últimos 6 a 12 meses."]),
    S("02", "Calcule as *horas disponíveis*", ["Horas de atendimento por dia, multiplicadas pelos dias de trabalho no mês e pelo número de cadeiras ou salas."]),
    S("03", "Ajuste pela *ocupação real*", ["Nenhuma clínica usa 100% da agenda.", "Se a ocupação média é de 70%, divida os custos fixos por 70% das horas disponíveis."]),
    S("04", "Use o número no *preço*", ["Custo da hora vezes o tempo do procedimento, mais materiais, impostos sobre a receita, taxas de cartão e repasse ao profissional."], box="Se o preço não cobre esse total, o procedimento consome margem, mesmo com agenda cheia."),
    A("Preço certo começa no custo certo", "Revise esse cálculo pelo menos uma vez por ano ou sempre que a estrutura mudar.", "Envie para o sócio da clínica"),
], """
Agenda cheia não garante lucro. Se o preço do procedimento não cobre o custo da hora clínica, cada atendimento consome margem.

O cálculo começa pelos custos fixos médios do mês, divididos pelas horas realmente ocupadas, considerando a taxa de ocupação da agenda. Esse custo por hora, multiplicado pelo tempo do procedimento, somado a materiais, impostos, taxas de cartão e repasse ao profissional, mostra o preço mínimo.

Revise esse número pelo menos uma vez por ano.

Salve para fazer a conta e compartilhe com o sócio da clínica.

#gestaodeclinicas #precificacao #clinicaodontologica #custos #contabilidade
"""),

]
