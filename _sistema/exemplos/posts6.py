from helpers import *

# Revisão com foco em clínicas odontológicas. Mesmo "tema" sobrescreve o post original.
POSTS = [

# ---------- SUBSTITUIÇÕES (antes: comércio) ----------

car("2026-11-21", "glosa-convenio", [
    C("Clínica com convênio", "Glosa de convênio: a receita que *some* sem ninguém ver", "Procedimento feito, nota emitida, valor que não entra.", "4 pontos para controlar"),
    S("01", "O que é", ["É o valor que a operadora do plano deixa de pagar, total ou parcialmente, por divergência na cobrança.", "O procedimento foi feito, mas o dinheiro não entra."]),
    S("02", "As causas *mais comuns*", ["Falta de autorização prévia, guia preenchida de forma incompleta, código de procedimento divergente da tabela e envio fora do prazo."]),
    S("03", "O efeito no *imposto*", ["Se a nota foi emitida pelo valor cheio e parte foi glosada, a clínica pode estar tributando receita que não recebeu.", "A baixa da glosa precisa estar registrada na contabilidade."]),
    S("04", "Como *controlar*", ["Concilie todo mês o que foi faturado e o que foi pago, por operadora.", "Acompanhe a taxa de glosa e recorra no prazo de cada contrato."], box="Uma taxa de glosa que ninguém mede é dinheiro perdido todo mês."),
    A("Meça a glosa da sua clínica", "Comece pela operadora com maior volume. O padrão costuma aparecer rápido.", "Envie para quem fatura os convênios"),
], """
A glosa é um dos vazamentos de receita mais comuns em clínicas odontológicas que atendem convênio.

O procedimento foi feito, a guia foi enviada, mas a operadora paga menos ou não paga. As causas mais frequentes são falta de autorização, guia incompleta, código divergente da tabela e envio fora do prazo. Se a nota foi emitida pelo valor cheio, a clínica ainda pode estar tributando uma receita que não recebeu.

A solução é conciliar todo mês o faturado e o pago, por operadora, e acompanhar a taxa de glosa.

Salve e envie para quem fatura os convênios da clínica.

#clinicaodontologica #convenio #glosa #gestaodeclinicas #contabilidadeparadentistas
"""),

car("2026-11-27", "repasse-dentista", [
    C("Gestão de clínicas", "Repasse ao dentista: como fazer *sem risco* fiscal", "O formato do repasse muda imposto, encargos e responsabilidade da clínica.", "Os 3 formatos e seus cuidados"),
    S("01", "Dentista *PJ*", [("Como funciona", "O dentista emite nota fiscal para a clínica pelo valor do repasse."), ("Cuidado", "Exija a nota todo mês. Repasse sem nota não comprova a despesa e fragiliza a relação.")]),
    S("02", "Dentista *autônomo*", [("Como funciona", "A clínica paga por RPA e retém INSS de 11% do profissional, além do Imposto de Renda pela tabela."), ("Cuidado", "Fora do Simples, a clínica ainda recolhe 20% de contribuição previdenciária sobre o valor.")]),
    S("03", "A *nota* para o paciente", ["Se a clínica emite a nota pelo valor total, ela tributa o valor cheio, inclusive a parte repassada.", "Esse ponto precisa estar claro no cálculo do percentual de repasse."]),
    S("04", "O *contrato*", ["Defina percentual, base de cálculo, prazo de pagamento e o que acontece com glosas e inadimplência.", "Autonomia real de agenda evita risco de vínculo."], box="Repasse sem contrato e sem documento fiscal é risco trabalhista e tributário ao mesmo tempo."),
    A("Revise o modelo de repasse", "O percentual certo depende de quem emite a nota e de quem paga os custos.", "Envie para o sócio da clínica"),
], """
O repasse ao dentista parceiro é rotina em quase toda clínica, e o formato escolhido muda o imposto e o risco.

Com dentista PJ, a clínica precisa da nota fiscal do repasse todo mês. Com autônomo, o pagamento é por RPA, com retenção de INSS e IR, e fora do Simples a clínica ainda recolhe 20% de contribuição previdenciária. E se a clínica emite a nota ao paciente pelo valor total, ela tributa também a parte repassada.

Tudo isso precisa estar no contrato e no cálculo do percentual.

Salve e envie para o sócio da clínica.

#clinicaodontologica #repasse #dentista #gestaodeclinicas #contabilidadeparadentistas
"""),

car("2026-12-14", "implante-orto-preco", [
    C("Precificação", "Implante e ortodontia: 4 erros de *preço e caixa*", "Tratamentos longos e parcelados escondem custo onde ninguém olha.", "Confira antes de fechar o próximo orçamento"),
    S("01", "Ignorar o *custo externo*", [("O problema", "Preço definido sem somar componentes, laboratório e materiais de alto valor."), ("O jeito certo", "Liste o custo direto de cada etapa antes de definir o valor ao paciente.")]),
    S("02", "Parcelar *sem calcular*", [("O problema", "Parcelamento longo no cartão sem juros para o paciente."), ("O jeito certo", "A taxa do parcelado sai da margem da clínica e precisa entrar no preço.")]),
    S("03", "Esquecer o *imposto*", [("O problema", "Tratar o valor recebido como lucro."), ("O jeito certo", "Reserve o imposto de cada recebimento. No Presumido, o regime de caixa pode ajudar em tratamentos parcelados, desde que haja controle.")]),
    S("04", "Manutenção *sem reajuste*", [("O problema", "Mensalidade de ortodontia com o mesmo valor por anos."), ("O jeito certo", "Revise o valor das manutenções pelo menos uma vez por ano.")], box="Tratamento parcelado é financiamento ao paciente. A clínica precisa saber quanto isso custa."),
    A("Refaça a conta dos tratamentos longos", "Comece pelo procedimento de maior volume na sua agenda.", "Envie para o sócio da clínica"),
], """
Implante e ortodontia são tratamentos de ticket alto, mas também os que mais escondem custo.

Os erros mais comuns: definir preço sem somar laboratório e componentes, parcelar no cartão sem calcular quanto a taxa consome, tratar o valor recebido como lucro sem reservar o imposto e manter a mensalidade da ortodontia sem reajuste por anos.

Tratamento parcelado é, na prática, um financiamento ao paciente. A clínica precisa saber o custo disso.

Salve e envie para o sócio da clínica.

#implantedentario #ortodontia #precificacao #clinicaodontologica #gestaodeclinicas
"""),

car("2026-12-30", "equipamento-clinica", [
    C("Planejamento 2027", "Vai comprar *equipamento* em 2027? Pense nisto antes", "Cadeira, raio-X, scanner intraoral: a forma de compra pesa no caixa e no imposto.", "4 pontos para decidir melhor"),
    S("01", "À vista ou *financiado*", ["Compare o desconto à vista com o custo total do financiamento.", "Comprometer o caixa de giro para economizar juros pode sair caro."]),
    S("02", "O efeito no *IR*", ["No Lucro Presumido, a depreciação do equipamento não reduz o IRPJ nem a CSLL.", "No Lucro Real, ela é dedutível ao longo da vida útil."]),
    S("03", "IBS e CBS na *compra*", ["No regime regular, compras de bens usados na atividade podem gerar crédito, desde que o fornecedor destaque e recolha o tributo.", "Peça a nota fiscal correta."]),
    S("04", "O *retorno*", ["Quantos procedimentos a mais o equipamento permite por mês?", "Quanto tempo leva para se pagar com a margem desses procedimentos?"], box="Equipamento bom é o que se paga. Faça a conta do retorno antes da compra."),
    A("Planeje a compra com números", "A decisão fica mais simples quando o retorno está calculado.", "Envie para o sócio da clínica"),
], """
Muitas clínicas planejam renovar equipamentos no início do ano. Antes de comprar, vale fazer quatro contas.

Compare o desconto à vista com o custo total do financiamento. Lembre que, no Lucro Presumido, a depreciação não reduz o IR, diferente do Lucro Real. A partir de 2027, no regime regular, a compra pode gerar crédito de IBS e CBS se o fornecedor destacar e recolher o tributo. E, principalmente, calcule em quanto tempo o equipamento se paga.

Salve e envie para o sócio da clínica.

#clinicaodontologica #equipamentoodontologico #planejamento2027 #gestaodeclinicas #contabilidadeparadentistas
"""),

img("2027-01-06", "cbs-clinica-presumido", {
    "theme": "white", "kicker": "Clínica no Lucro Presumido",
    "title": "Em 2027, sua clínica troca PIS e Cofins pela *CBS*",
    "text": "Os 3,65% cumulativos dão lugar a um tributo com direito a crédito. Serviços de saúde listados na LC 214/2025 têm redução de 60% na alíquota.",
    "box": "Confira se os serviços da clínica estão corretamente classificados nas notas fiscais.",
}, """
Para a clínica odontológica no Lucro Presumido, 2027 traz uma mudança direta: PIS e Cofins, que somavam 3,65% sobre a receita sem direito a crédito, dão lugar à CBS.

A CBS funciona com crédito sobre compras e tem redução de 60% para os serviços de saúde listados na LC 214/2025, entre eles a odontologia. A alíquota de referência ainda depende de resolução do Senado, e o enquadramento depende da classificação correta dos serviços na nota.

Salve e compartilhe com o sócio da clínica.

#clinicaodontologica #cbs #lucropresumido #reformatributaria #contabilidadeparadentistas
"""),

# ---------- REESCRITAS ----------

car("2026-11-05", "o-que-a-smartcontax-faz", [
    C("Prazer, Smartcontax", "Contabilidade para *clínicas odontológicas* que querem decidir com números", "Do imposto correto à gestão da clínica.", "4 coisas que entregamos além da guia do mês"),
    S("01", "Imposto *calculado* e conferido", [("O que fazemos", "Apuração mensal, obrigações acessórias e conferência das notas da clínica."), ("Por que importa", "Erro de enquadramento não aparece no mês. Aparece na fiscalização, com juros e multa.")]),
    S("02", "Regime tributário *revisado*", [("O que fazemos", "Comparamos Simples, Presumido e equiparação hospitalar com os números reais da clínica."), ("Por que importa", "Regime escolhido na abertura costuma ficar caro quando a clínica cresce.")]),
    S("03", "Números da *clínica*", [("O que fazemos", "Organizamos faturamento, repasses, custos e margem de forma que o sócio consiga ler."), ("Por que importa", "Contratar, investir em equipamento ou retirar lucro dependem desses números.")]),
    S("04", "Atendimento *onde você está*", [("Como funciona", "Contabilidade 100% digital. Falamos por WhatsApp, videochamada ou vamos até a sua clínica.")], box="Você não precisa sair da clínica para ter um contador presente."),
    A("Conheça a forma como trabalhamos", "Siga o @smartcontax para receber conteúdo sobre impostos, gestão de clínicas e Reforma Tributária de segunda a sexta.", "Envie para um colega dono de clínica"),
], """
A maioria dos donos de clínica só fala com o contador quando chega a guia para pagar.

A Smartcontax é uma contabilidade focada em clínicas odontológicas e da área da saúde. Além de apurar impostos e cumprir obrigações, revisamos o regime tributário, organizamos faturamento, repasses e margem para que o sócio consiga ler os números, e atendemos onde você estiver: WhatsApp, videochamada ou na sua clínica.

Salve este post e acompanhe o perfil: a partir de hoje, conteúdo novo de segunda a sexta.

#contabilidadeparadentistas #clinicaodontologica #contabilidadeconsultiva #gestaodeclinicas #smartcontax
"""),

car("2026-11-09", "pro-labore-x-lucros", [
    C("Sócios da clínica", "Dentista sócio: pró-labore ou *distribuição de lucros*?", "As duas formas são legais. O erro está em usar uma no lugar da outra.", "O que diferencia cada uma e quando usar"),
    S("01", "Pró-labore", [("O que é", "A remuneração pelo trabalho do sócio na clínica, inclusive pelos atendimentos que ele faz."), ("O que incide", "INSS de 11% descontado do sócio, até o teto, e Imposto de Renda pela tabela. Fora do Simples, a clínica recolhe 20% de contribuição previdenciária.")]),
    S("02", "Distribuição de lucros", [("O que é", "A divisão do resultado que a clínica gerou."), ("O que incide", "Não tem INSS. Desde 2026, valores acima de R$ 50 mil por mês, pagos pela mesma empresa à mesma pessoa, têm retenção de 10% de IR (Lei 15.270/2025).")]),
    S("03", "O erro *mais comum*", ["Sócio que atende na cadeira todos os dias e retira tudo como lucro, sem pró-labore.", "Nesse caso, há risco de a Receita requalificar os valores e cobrar INSS."]),
    S("04", "O jeito certo", ["Pró-labore compatível com o trabalho de cada sócio.", "Lucro distribuído com base na contabilidade, depois de apurado."], box="Sem escrituração contábil, a distribuição isenta fica limitada à base presumida, descontados os impostos."),
    A("Retirada com regra é retirada segura", "O valor ideal depende do regime, da folha e do lucro apurado da clínica.", "Envie para o seu sócio"),
], """
Na clínica em que os sócios também atendem, a forma de retirar dinheiro precisa de atenção.

Pró-labore remunera o trabalho do sócio, inclusive na cadeira, e tem INSS e IR. Distribuição de lucros divide o resultado da clínica, sem INSS, mas desde 2026 tem retenção de 10% de IR quando passa de R$ 50 mil por mês para a mesma pessoa, conforme a Lei 15.270/2025.

O erro mais comum é o sócio que atende todos os dias e retira tudo como lucro. Outro é distribuir lucro sem contabilidade que comprove o resultado.

Salve para consultar e envie para o seu sócio.

#prolabore #distribuicaodelucros #clinicaodontologica #socios #contabilidadeparadentistas
"""),

car("2026-11-10", "conta-pf-pj-misturada", [
    C("Erros de gestão", "Conta da clínica e conta pessoal *misturadas*", "Parece prático. Custa caro depois.", "4 riscos e como corrigir"),
    S("01", "Você perde o *controle real*", [("O problema", "Maquininha da clínica caindo na conta pessoal ou despesas da casa pagas pela clínica."), ("O risco", "Ninguém sabe quanto a clínica lucrou de verdade.")]),
    S("02", "Retirada vira *problema fiscal*", [("O problema", "Dinheiro que sai sem classificação."), ("O risco", "Pode ser tratado como remuneração sem INSS e IR, ou como receita omitida.")]),
    S("03", "A contabilidade *não fecha*", [("O problema", "Extrato com despesas que não são da clínica."), ("O risco", "Balanço sem credibilidade para banco, financiamento de equipamento ou entrada de novo sócio.")]),
    S("04", "O patrimônio *se confunde*", [("O problema", "Bens e dívidas do sócio e da clínica no mesmo lugar."), ("O risco", "Em discussões judiciais, a confusão patrimonial pode atingir os bens pessoais do sócio.")], box="O jeito certo: defina um pró-labore, transfira para a conta pessoal e pague as despesas pessoais de lá."),
    A("Separar é o primeiro passo da gestão", "Uma retirada fixa por mês já resolve a maior parte do problema.", "Envie para um colega dono de clínica"),
], """
Receber o cartão da clínica na conta pessoal ou pagar a conta de casa pela clínica parece não ter consequência. Tem.

Quando as contas se misturam, você perde a noção do lucro real, a contabilidade deixa de refletir a clínica e as retiradas sem classificação podem virar problema fiscal. Na hora de financiar um equipamento ou receber um novo sócio, o balanço perde credibilidade.

A correção é simples: defina um pró-labore, transfira esse valor para a sua conta pessoal e pague suas despesas de lá.

Salve e compartilhe com quem ainda mistura as contas.

#clinicaodontologica #gestaofinanceira #gestaodeclinicas #fluxodecaixa #contabilidadeparadentistas
"""),

car("2026-11-16", "13-salario-guia", [
    C("Equipe da clínica", "13º salário da equipe: *prazos* e cálculo sem erro", "ASB, TSB, recepção e limpeza: as regras valem para todos os CLT.", "Guia rápido para o sócio da clínica"),
    S("01", "Os *prazos*", [("1ª parcela", "Até 30 de novembro."), ("2ª parcela", "Até 20 de dezembro. Em 2026 a data cai em um domingo, então o pagamento deve ser feito até sexta-feira, 18/12.")]),
    S("02", "Como *calcular*", ["O 13º é proporcional: 1/12 do salário para cada mês trabalhado no ano.", "Conta como mês completo aquele em que o funcionário trabalhou 15 dias ou mais."]),
    S("03", "O que *entra* na base", ["Salário e médias de variáveis habituais, como horas extras, adicional de insalubridade e comissões."]),
    S("04", "Os *descontos*", ["A 1ª parcela corresponde à metade do valor, sem descontos de INSS e IR.", "Os descontos são feitos na 2ª parcela. O FGTS incide sobre as duas."], box="Dentista parceiro PJ ou autônomo não recebe 13º. Se a relação tiver cara de vínculo, o risco é outro."),
    A("Dezembro pesa no caixa da clínica", "13º, férias e encargos se concentram no fim do ano. Planejar agora evita aperto.", "Envie para quem cuida da folha"),
], """
O 13º salário da equipe da clínica tem duas datas: 1ª parcela até 30 de novembro e 2ª parcela até 20 de dezembro. Como 20/12/2026 cai em um domingo, a 2ª parcela deve ser paga até sexta-feira, 18/12.

O valor é proporcional aos meses trabalhados e inclui médias de variáveis habituais, como horas extras e adicional de insalubridade. A 1ª parcela é metade do valor, sem descontos. INSS e IR são descontados na 2ª. O FGTS incide nas duas.

Salve para consultar e envie para quem cuida da folha da clínica.

#13salario #clinicaodontologica #departamentopessoal #gestaodeclinicas #contabilidadeparadentistas
"""),

car("2026-11-23", "credito-ibs-cbs", [
    C("Reforma para clínicas", "Crédito de IBS e CBS: o que muda na conta da *clínica*", "A Reforma amplia a não cumulatividade. Entenda o que isso significa.", "Explicado com um exemplo simples"),
    S("01", "Como é *hoje*", ["Clínicas no Lucro Presumido pagam PIS e Cofins no regime cumulativo, com 3,65% sobre a receita e sem crédito sobre compras."]),
    S("02", "Como *fica*", ["Com CBS e IBS, a regra geral é a não cumulatividade ampla.", "O tributo pago em compras como materiais, equipamentos e serviços vira crédito, com exceções previstas em lei."]),
    S("03", "Um *exemplo*", ["A clínica compra R$ 1.000 em materiais com R$ 100 de tributo destacado e deve R$ 200 de tributo sobre os atendimentos.", "Ela recolhe a diferença: R$ 100."]),
    S("04", "O que isso *exige*", ["Fornecedores de materiais e laboratórios regulares, com nota fiscal correta.", "Controle das compras que geram crédito e das que não geram."], box="Valores ilustrativos. As alíquotas de referência ainda serão definidas, e o crédito depende do pagamento do tributo pelo fornecedor."),
    A("Fornecedor passa a pesar no imposto", "Comprar de quem não destaca o tributo corretamente pode significar perder crédito a partir de 2027.", "Envie para quem faz as compras da clínica"),
], """
Uma das mudanças mais relevantes da Reforma Tributária para a clínica é a não cumulatividade ampla.

Hoje, clínicas no Lucro Presumido pagam PIS e Cofins sobre a receita, sem crédito nas compras. Com CBS e IBS, o tributo pago em materiais, equipamentos e serviços de laboratório passa a gerar crédito, com exceções previstas em lei.

Isso muda a importância do fornecedor. Comprar de quem não emite nota correta pode significar perder crédito.

Os valores do exemplo são ilustrativos. Salve e envie para quem faz as compras da clínica.

#reformatributaria #ibs #cbs #clinicaodontologica #contabilidadeparadentistas
"""),

car("2026-11-24", "sinais-regime-errado", [
    C("Gestão tributária", "5 sinais de que sua clínica pode estar no *regime errado*", "Regime tributário não é escolha para a vida toda.", "Se você se identificou com 2 ou mais, vale revisar"),
    S("01", "O faturamento *mudou muito*", ["A clínica abriu com uma cadeira e hoje tem três ou quatro.", "As faixas do Simples e as bases do Presumido reagem de forma diferente ao crescimento."]),
    S("02", "A folha *cresceu ou encolheu*", ["Na odontologia, a relação entre folha e faturamento define o anexo do Simples pelo Fator R.", "Contratar ASB ou trocar CLT por parceiros pode mudar o imposto."]),
    S("03", "Ninguém olhou a *equiparação*", ["Clínicas que fazem procedimentos podem ter base menor de IRPJ e CSLL no Presumido, se cumprirem os requisitos."]),
    S("04", "A margem *não fecha*", ["Agenda cheia, caixa apertado e nenhuma explicação clara.", "Imposto é um dos primeiros itens a investigar."]),
    S("05", "Você não sabe *quanto paga*", ["Se você não sabe qual percentual do faturamento vai para impostos, não consegue saber se esse número é justo."], box="A entrada no Simples agora tem prazo em setembro. Quem perde a janela só muda no ano seguinte."),
    A("Revise com antecedência", "A escolha do regime vale para o ano inteiro. A análise precisa vir meses antes do prazo, não na véspera.", "Envie para um colega dono de clínica"),
], """
Regime tributário escolhido na abertura da clínica e nunca revisado é um dos erros mais comuns que encontramos.

A clínica cresce, a folha muda, a margem aperta, e o enquadramento continua o mesmo. Na odontologia, o Fator R define o anexo do Simples. No Presumido, a equiparação hospitalar pode reduzir a base de IRPJ e CSLL para quem faz procedimentos.

Desde a LC 214/2025, a opção pelo Simples Nacional é feita em setembro, para valer no ano seguinte. Para o Presumido e o Real, a escolha se confirma no primeiro pagamento do ano. Em qualquer caso, a análise precisa vir antes do prazo.

Salve e compartilhe com quem precisa fazer essa revisão.

#regimetributario #clinicaodontologica #simplesnacional #lucropresumido #contabilidadeparadentistas
"""),

car("2026-12-01", "checklist-dezembro", [
    C("Planejamento 2027", "Checklist de dezembro para a clínica *começar 2027* organizada", "O que fazer agora evita retrabalho e imposto a mais em janeiro.", "6 itens para conferir este mês"),
    S("01", "Revisar o *regime tributário*", ["Simule Presumido, com e sem equiparação hospitalar, e Real com os números de 2026.", "Fora do Simples, a escolha se confirma no primeiro pagamento de 2027. A entrada no Simples teve prazo em setembro."]),
    S("02", "Atualizar o *sistema de notas*", ["Confirme com o fornecedor se o emissor de NFS-e da clínica está preparado para IBS e CBS em 2027."]),
    S("03", "Planejar as *retiradas*", ["Defina pró-labore e distribuição de lucros dos sócios para 2027, considerando a Lei 15.270/2025."]),
    S("04", "Organizar a *folha*", ["13º, férias e encargos da equipe no caixa de dezembro.", "Revise salários e o reajuste previsto na convenção coletiva."]),
    S("05", "Conferir *licenças e cadastros*", ["Licença sanitária, registro da clínica no CRO, alvará, certificado digital e certidões com validade."]),
    S("06", "Conciliar *recebimentos*", ["Cartão a receber, convênios, glosas e parcelamentos de tratamento.", "O balanço de 2026 depende dessa conferência."], box="Um dezembro organizado é o que permite um balanço confiável e decisões melhores em 2027."),
    A("Use como lista de tarefas", "Marque cada item ao longo do mês. Os mais urgentes são o regime e o sistema de notas.", "Envie para o seu sócio"),
], """
Dezembro é o mês que define como a clínica começa o ano seguinte.

Seis itens para conferir: regime tributário de 2027, sistema de notas preparado para IBS e CBS, retiradas dos sócios, folha de dezembro, validade de licenças, registro no CRO e certificado digital, e conciliação de cartão, convênios, glosas e parcelamentos.

Os dois mais urgentes são o regime e o sistema de notas, porque dependem de decisão antes de janeiro.

Salve como lista de tarefas e compartilhe com o seu sócio.

#clinicaodontologica #planejamentotributario #fechamentodeano #gestaodeclinicas #contabilidadeparadentistas
"""),

car("2026-12-03", "confraternizacao-brindes", [
    C("Fim de ano na clínica", "Confraternização da equipe e brindes a pacientes: o que a lei *permite*", "Cuidados fiscais com as despesas de dezembro.", "Depende do regime da sua clínica"),
    S("01", "Simples e *Presumido*", ["Nesses regimes, o imposto é calculado sobre o faturamento.", "As despesas não reduzem o IR, mas precisam ser da clínica e estar documentadas."]),
    S("02", "Lucro Real: *brindes*", ["Brindes a pacientes são indedutíveis para IRPJ e CSLL, conforme a Lei 9.249/1995.", "O gasto pode ser feito, mas não reduz o imposto."]),
    S("03", "Lucro Real: *equipe*", ["Despesas com confraternização dos funcionários tendem a ser aceitas quando ligadas à atividade, oferecidas a todos e bem documentadas."]),
    S("04", "Em *qualquer* regime", ["Exija nota fiscal em nome da clínica.", "Não misture despesas pessoais dos sócios com despesas da clínica."], box="Despesa sem documento ou sem relação com a atividade pode ser glosada em fiscalização."),
    A("Celebre com segurança", "Nota fiscal em nome da clínica é o mínimo para qualquer despesa de fim de ano.", "Envie para quem organiza a confraternização"),
], """
Confraternização da equipe e brindes para pacientes são despesas comuns em dezembro, e o tratamento fiscal depende do regime da clínica.

No Simples e no Presumido, o imposto é calculado sobre o faturamento, então as despesas não reduzem o IR, mas precisam ser da clínica e estar documentadas. No Lucro Real, brindes são indedutíveis conforme a Lei 9.249/1995, enquanto despesas com a equipe tendem a ser aceitas quando oferecidas a todos e bem documentadas.

Em qualquer regime: nota fiscal em nome da clínica e nada de despesa pessoal no meio.

Salve e compartilhe com quem organiza o fim de ano.

#clinicaodontologica #fimdeano #gestaodeclinicas #despesasdedutiveis #contabilidadeparadentistas
"""),

img("2026-12-11", "faturamento-2026-define-2027", {
    "theme": "navy", "kicker": "Planejamento da clínica",
    "title": "O faturamento de *2026* define o planejamento de *2027*",
    "text": "Fator R, base do Presumido, equiparação hospitalar e projeção da CBS: tudo parte dos números deste ano.",
    "box": "Simulação feita com números antigos leva a decisões erradas.",
}, """
O planejamento tributário da clínica para 2027 começa pelos números de 2026.

No Simples, a alíquota e o Fator R são calculados sobre os últimos 12 meses. No Presumido, a comparação com e sem equiparação hospitalar depende da receita de procedimentos. E a projeção da CBS em 2027 também parte do faturamento atual.

Por isso, a contabilidade da clínica precisa estar em dia agora, e não em março.

Salve e compartilhe com o seu sócio.

#clinicaodontologica #planejamentotributario #regimetributario #contabilidadeparadentistas
"""),

car("2026-12-10", "split-payment", [
    C("Reforma Tributária", "Split payment: o imposto *separado* no pagamento do paciente", "Uma das mudanças que mais vão afetar o caixa da clínica.", "Entenda em 4 pontos"),
    S("01", "O que é", ["Um mecanismo previsto na LC 214/2025 em que o IBS e a CBS são separados no momento do pagamento.", "O valor do tributo vai direto para o fisco, sem passar pela conta da clínica."]),
    S("02", "Como *funciona*", ["Quando o paciente paga por cartão, PIX ou boleto, o sistema de pagamento separa a parte do tributo.", "A clínica recebe o valor líquido."]),
    S("03", "O efeito no *caixa*", ["Hoje, muitas clínicas usam o imposto recebido como capital de giro até o vencimento da guia.", "Com o split payment, esse dinheiro deixa de passar pelo caixa."]),
    S("04", "Quando *começa*", ["A implantação será gradual e ainda depende de regulamentação e de adaptação dos sistemas de pagamento."], box="O momento de rever o capital de giro da clínica é antes do split payment começar."),
    A("Prepare o caixa para a mudança", "Clínicas que dependem do imposto como capital de giro são as mais afetadas.", "Envie para quem cuida do financeiro"),
], """
O split payment é um dos pontos da Reforma Tributária com maior impacto no caixa da clínica.

Previsto na LC 214/2025, ele separa o IBS e a CBS no momento em que o paciente paga: o tributo vai direto para o fisco e a clínica recebe o valor líquido. Para quem usa o imposto recebido como capital de giro até o vencimento da guia, isso muda a dinâmica do caixa.

A implantação será gradual e ainda depende de regulamentação, mas o planejamento precisa começar antes.

Salve e compartilhe com quem cuida do financeiro da clínica.

#splitpayment #reformatributaria #clinicaodontologica #fluxodecaixa #contabilidadeparadentistas
"""),

car("2026-12-15", "carga-efetiva", [
    C("Gestão tributária", "Quanto sua clínica *pagou de imposto* em 2026?", "Saber esse número é o primeiro passo para avaliar se ele está correto.", "Como calcular a carga efetiva"),
    S("01", "Some todos os *tributos*", ["Sobre a receita: DAS, ou ISS, PIS, Cofins, IRPJ e CSLL no Presumido.", "Sobre a folha: INSS patronal e FGTS da equipe."]),
    S("02", "Divida pelo *faturamento*", ["Total de tributos do ano dividido pela receita bruta do ano.", "O resultado é a carga tributária efetiva, em percentual."]),
    S("03", "Compare com o *esperado*", ["O percentual é compatível com o regime e com os serviços da clínica?", "Clínica que faz procedimentos e não usa equiparação hospitalar, por exemplo, pode estar pagando mais do que precisa."]),
    S("04", "Use para *decidir*", ["É com esse número que se compara regimes, se revisa o preço dos procedimentos e se projeta 2027."], box="Se ninguém consegue te dizer esse percentual, a clínica está sem uma informação básica de gestão."),
    A("Peça esse número ao seu contador", "Carga tributária efetiva é o ponto de partida de qualquer planejamento.", "Envie para o seu sócio"),
], """
Você sabe qual percentual do faturamento da sua clínica foi para impostos em 2026?

A conta é simples: some todos os tributos pagos no ano, sobre a receita e sobre a folha, e divida pela receita bruta. O resultado é a carga tributária efetiva. É com ele que se compara regimes, se revisa o preço dos procedimentos e se projeta o ano seguinte.

Se ninguém consegue te informar esse número, comece por ele.

Salve e compartilhe com o seu sócio.

#cargatributaria #clinicaodontologica #planejamentotributario #contabilidadeparadentistas
"""),

car("2026-12-16", "sistema-notas-2027", [
    C("Reforma Tributária", "O emissor de notas da sua clínica está pronto para *2027*?", "Nota fiscal com IBS e CBS errados vira problema desde o primeiro dia.", "O que perguntar ao fornecedor do sistema"),
    S("01", "Campos de *IBS e CBS*", ["O sistema da clínica já preenche os grupos de IBS e CBS na NFS-e?", "Se a clínica vende produtos, também na NF-e ou NFC-e."]),
    S("02", "Classificação *tributária*", ["Cada serviço precisa ter CST e código de classificação tributária (cClassTrib) corretos.", "É ele que aplica a redução de 60% para saúde."]),
    S("03", "Código do *serviço*", ["A NBS dos serviços odontológicos precisa estar correta.", "Serviço classificado errado pode perder a redução."]),
    S("04", "Testes", ["Peça para emitir notas de teste e confira o XML com o seu contador antes de janeiro."], box="Não presuma que o sistema foi atualizado. Peça a confirmação por escrito."),
    A("Valide antes da virada", "Em 2027 a CBS passa a ser cobrada. Nota errada significa imposto errado.", "Envie para quem emite as notas da clínica"),
], """
Em 2027 a CBS passa a ser cobrada de verdade, e a nota fiscal da clínica é onde tudo começa.

Pergunte ao fornecedor do sistema: os campos de IBS e CBS já são preenchidos na NFS-e? Cada serviço tem CST, cClassTrib e NBS corretos? É essa classificação que aplica a redução de 60% prevista para os serviços de saúde.

Peça notas de teste e confira o XML com o seu contador antes de janeiro. E peça a confirmação por escrito.

Salve e envie para quem emite as notas da clínica.

#reformatributaria #nfse #clinicaodontologica #cclasstrib #contabilidadeparadentistas
"""),

car("2026-12-21", "irpf-socio-organizar", [
    C("Imposto de Renda", "Dentista sócio: comece a organizar o *IR de 2027* agora", "A declaração de 2027 se refere ao que aconteceu em 2026.", "O que separar ainda em dezembro"),
    S("01", "Informes da *clínica*", ["Pró-labore e lucros recebidos em 2026, com os valores de IR retido.", "Peça ao contador o informe de rendimentos da clínica."]),
    S("02", "Atendimentos como *PF*", ["Se você também atende como pessoa física em outro lugar, reúna o carnê-leão e o livro-caixa do ano."]),
    S("03", "Bens e *despesas*", ["Compras e vendas de imóveis, veículos e participações.", "Despesas dedutíveis com saúde, educação e previdência PGBL."]),
    S("04", "Renda *alta*", ["Com a Lei 15.270/2025, rendas totais acima de R$ 600 mil no ano passam a ter imposto mínimo.", "Lucros recebidos da clínica entram nessa conta."], box="Declaração feita com pressa no último mês tem mais chance de cair na malha."),
    A("Organize antes do prazo", "Quanto antes os documentos estiverem reunidos, mais tempo para revisar com calma.", "Envie para o seu sócio"),
], """
A declaração de Imposto de Renda de 2027 se refere ao ano de 2026, e o dentista sócio que organiza tudo em dezembro declara com mais segurança.

Separe os informes de pró-labore e lucros recebidos da clínica, o carnê-leão e o livro-caixa se também atende como pessoa física, os informes de bancos e corretoras e as despesas dedutíveis. Para rendas totais acima de R$ 600 mil no ano, a Lei 15.270/2025 criou o imposto mínimo, e os lucros da clínica entram nessa conta.

Salve e compartilhe com o seu sócio.

#impostoderenda #dentista #irpf #clinicaodontologica #contabilidadeparadentistas
"""),

car("2026-12-22", "3-perguntas-2027", [
    C("Planejamento da clínica", "3 perguntas para fazer *antes de 2027*", "Planejamento começa com perguntas certas, não com planilhas.", "Responda com seu sócio"),
    S("01", "Para onde a clínica vai se *nada mudar*?", ["Projete o próximo ano com o mesmo ritmo de agenda, custos, repasses e retiradas.", "Se o resultado não agrada, algo precisa mudar agora."]),
    S("02", "Qual decisão foi *adiada* em 2026?", ["Reajustar preços, contratar, abrir mais uma cadeira, sair de um convênio que paga pouco, revisar o regime.", "Decisão adiada também tem custo."]),
    S("03", "Que número você vai *acompanhar*?", ["Escolha um ou dois indicadores para olhar todo mês em 2027: ocupação da agenda, ticket médio, glosa ou margem."], box="Escreva as respostas. Decisão que fica só na cabeça raramente vira ação em janeiro."),
    A("Comece 2027 com clareza", "Três respostas honestas valem mais que um planejamento longo que ninguém segue.", "Envie para o seu sócio"),
], """
Antes de montar qualquer planilha para 2027, responda três perguntas com o seu sócio.

Para onde a clínica vai se nada mudar? Qual decisão importante foi adiada em 2026, como reajustar preços, abrir mais uma cadeira ou sair de um convênio que paga pouco? Que número vocês vão acompanhar todo mês no próximo ano?

As respostas mostram o que precisa ser feito em janeiro. E escreva: decisão que fica só na cabeça raramente vira ação.

Salve e compartilhe com o seu sócio.

#clinicaodontologica #planejamento #gestaodeclinicas #metas2027
"""),

img("2026-12-23", "das-dezembro-janeiro", {
    "theme": "light", "kicker": "Recesso não é pausa fiscal",
    "title": "Os impostos de *dezembro* da clínica vencem em *janeiro*",
    "text": "No Presumido, PIS e Cofins vencem no dia 25, e IRPJ e CSLL do 4º trimestre no último dia útil de janeiro. No Simples, o DAS vence no dia 20.",
    "box": "Dezembro costuma ter faturamento maior, e o imposto de janeiro acompanha.",
}, """
Os impostos sobre o faturamento de dezembro da clínica vencem em janeiro.

No Lucro Presumido, PIS e Cofins vencem no dia 25 e IRPJ e CSLL do 4º trimestre vencem no último dia útil de janeiro. No Simples Nacional, o DAS vence no dia 20. O ISS segue o calendário do município.

Como dezembro costuma ter faturamento maior, a conta de janeiro chega justamente depois de 13º, férias e despesas de fim de ano. Reserve o valor ainda em dezembro.

Salve e compartilhe com quem cuida do financeiro da clínica.

#clinicaodontologica #lucropresumido #fluxodecaixa #prazos #contabilidadeparadentistas
"""),

car("2027-01-05", "decisoes-janeiro", [
    C("Começo de ano", "5 decisões da clínica que *não podem esperar* fevereiro", "Janeiro define boa parte do resultado do ano.", "Confira se a sua clínica já resolveu"),
    S("01", "Regime tributário", ["Fora do Simples, a escolha entre Presumido e Real se confirma com o primeiro pagamento do ano. A análise precisa estar feita antes dele."]),
    S("02", "Pró-labore e *retiradas*", ["Definir valores para 2027, considerando o Fator R e as regras de distribuição de lucros."]),
    S("03", "Tabela de *preços*", ["Revisar procedimentos com custos de materiais e laboratório reajustados, taxas de cartão e efeitos da CBS."]),
    S("04", "Notas fiscais", ["Confirmar que as notas emitidas em janeiro estão com IBS, CBS e a redução de saúde corretos."]),
    S("05", "Metas", ["Definir os indicadores da clínica que serão acompanhados todo mês e quem é responsável por cada um."], box="Uma reunião de 1 hora com o seu contador em janeiro pode evitar meses de ajustes."),
    A("Resolva em janeiro", "Cada mês de atraso em uma decisão tributária é um mês pagando pelo caminho errado.", "Envie para o seu sócio"),
], """
Janeiro concentra decisões que definem o resultado da clínica no ano inteiro.

Regime tributário, para quem está no Presumido ou no Real, que confirmam a escolha no primeiro pagamento do ano. Pró-labore e retiradas para 2027. Revisão da tabela de procedimentos com custos reajustados e os efeitos da CBS. Conferência das notas emitidas no novo modelo. E definição dos indicadores que serão acompanhados.

Uma reunião de 1 hora com o contador em janeiro pode evitar meses de ajustes.

Salve e compartilhe com o seu sócio.

#clinicaodontologica #planejamento2027 #regimetributario #gestaodeclinicas #contabilidadeparadentistas
"""),

car("2027-01-08", "orcamento-anual", [
    C("Planejamento 2027", "Como montar o *orçamento* da clínica para 2027", "Um orçamento simples já muda a qualidade das decisões do ano.", "5 passos práticos"),
    S("01", "Projete a *receita*", ["Parta do faturamento de 2026, mês a mês, separando particular e convênio.", "Considere férias, sazonalidade e a capacidade real da agenda."]),
    S("02", "Liste os *custos fixos*", ["Aluguel, folha da equipe, pró-labore, sistemas, contabilidade e manutenção.", "Inclua reajustes previstos para o ano."]),
    S("03", "Estime os *variáveis*", ["Materiais, laboratório, repasses, impostos sobre a receita e taxas de cartão, em percentual da receita."]),
    S("04", "Separe os *investimentos*", ["Equipamentos, reformas, marketing e contratações planejadas, com o mês previsto."]),
    S("05", "Acompanhe todo *mês*", ["Compare o realizado com o orçado e ajuste a rota a cada trimestre."], box="Orçamento não é previsão perfeita. É uma referência para perceber cedo quando algo sai do esperado."),
    A("Planeje com números reais", "Use a contabilidade de 2026 como base, não estimativas de memória.", "Envie para o seu sócio"),
], """
Um orçamento simples já muda a forma como a clínica toma decisões ao longo do ano.

Projete a receita mês a mês, separando particular e convênio. Liste os custos fixos com reajustes, estime materiais, laboratório, repasses e impostos em percentual da receita, separe os investimentos com o mês previsto e compare o realizado com o orçado todo mês.

O orçamento não precisa acertar tudo. Ele existe para mostrar cedo quando algo sai do esperado.

Salve e compartilhe com o seu sócio.

#clinicaodontologica #orcamento #planejamento2027 #gestaodeclinicas #contabilidadeparadentistas
"""),

car("2027-01-11", "4-numeros-semana", [
    C("Gestão da clínica", "4 números que o dono da clínica deve olhar *toda semana*", "Não é preciso ser financeiro para acompanhar o essencial.", "Leva menos de 15 minutos"),
    S("01", "Saldo de *caixa*", ["Quanto há disponível hoje em todas as contas da clínica.", "Compare com o da semana anterior para entender a tendência."]),
    S("02", "Contas a *receber*", ["Cartão a receber, convênios a pagar, parcelamentos de tratamento e boletos de pacientes."]),
    S("03", "Contas a *pagar*", ["O que vence nos próximos 30 dias: folha, repasses, laboratório, impostos e aluguel.", "Janeiro concentra os impostos sobre o faturamento de dezembro."]),
    S("04", "Agenda e *faturamento*", ["Quanto a clínica faturou no mês até agora e quanto da agenda está ocupado.", "Compare com a meta e com o mesmo período do mês anterior."], box="Saldo + a receber − a pagar mostra se a clínica fecha o mês no positivo. Esse é o número que evita susto."),
    A("Gestão começa por rotina", "Escolha um dia fixo da semana e reserve 15 minutos para esses quatro números.", "Envie para o sócio da clínica"),
], """
Você não precisa de um relatório de 20 páginas para saber como a clínica está. Quatro números, olhados toda semana, resolvem a maior parte das decisões.

Saldo de caixa, contas a receber (cartão, convênios e parcelamentos), contas a pagar nos próximos 30 dias (folha, repasses, laboratório e impostos) e faturamento com ocupação da agenda. Com esses quatro, você sabe se fecha o mês no positivo e tem tempo de agir se não fechar.

Em janeiro isso é ainda mais importante, porque os impostos sobre o faturamento de dezembro vencem agora.

Salve e reserve 15 minutos fixos na sua semana.

#clinicaodontologica #gestaofinanceira #fluxodecaixa #gestaodeclinicas #contabilidadeparadentistas
"""),

img("2027-01-12", "checklist-documentos-mes", {
    "theme": "white", "kicker": "Rotina mensal da clínica",
    "title": "O que a clínica deve enviar ao contador *todo mês*",
    "text": "• Extratos de todas as contas e da maquininha\n• Notas emitidas e notas de fornecedores\n• Relatório de convênios: faturado, pago e glosado\n• Repasses aos dentistas, com nota ou RPA\n• Admissões, demissões e alterações na folha",
    "box": "Documento que chega atrasado vira imposto calculado com informação incompleta.",
}, """
A qualidade da contabilidade da clínica depende da qualidade da informação que chega até ela.

Todo mês, cinco grupos de documentos são essenciais: extratos das contas e da maquininha, notas emitidas e de fornecedores, relatório de convênios com o que foi faturado, pago e glosado, repasses aos dentistas com nota ou RPA, e movimentações da folha.

Sem isso, o imposto é calculado com informação incompleta e o balanço deixa de representar a clínica.

Salve este checklist e deixe no calendário mensal da clínica.

#clinicaodontologica #rotinacontabil #gestaodeclinicas #contabilidadeparadentistas
"""),

car("2027-01-13", "taxas-cartao", [
    C("Gestão financeira", "Taxas de cartão: o custo que *a clínica não revisa*", "Pequenos percentuais sobre todo o faturamento viram um valor relevante no ano.", "4 pontos para conferir na maquininha"),
    S("01", "Taxa por *modalidade*", ["Débito, crédito à vista e parcelado têm taxas diferentes.", "Confira se o que está no extrato é o que foi contratado."]),
    S("02", "Antecipação", ["Receber antes do prazo tem custo, que funciona como juros sobre o valor antecipado.", "Antecipação automática costuma estar ativada sem que o sócio saiba."]),
    S("03", "Tratamento em *10x sem juros*", ["Quando a clínica parcela implante ou ortodontia sem juros, quem paga a taxa do parcelamento é a clínica.", "Esse custo precisa estar no preço."]),
    S("04", "Faça a *conta anual*", ["Some todas as taxas pagas no ano e compare com o faturamento no cartão.", "Com esse número, negocie ou compare com outras empresas de pagamento."], box="Taxa de cartão é custo variável e precisa entrar no cálculo da margem de cada procedimento."),
    A("Revise o contrato da maquininha", "Uma renegociação pode render mais que muitos cortes de despesa.", "Envie para quem cuida do financeiro"),
], """
A taxa de cartão parece pequena porque é cobrada em percentual. Somada ao longo do ano, sobre todo o faturamento da clínica, costuma virar um dos maiores custos variáveis.

Confira se as taxas por modalidade correspondem ao contrato, se a antecipação automática está ativada sem necessidade e se o custo de parcelar implante e ortodontia sem juros está no preço. Depois, some as taxas pagas no ano e use o número para negociar.

Salve e envie para quem cuida do financeiro da clínica.

#clinicaodontologica #taxasdecartao #gestaofinanceira #precificacao #contabilidadeparadentistas
"""),

img("2027-01-19", "o-que-e-dre", {
    "theme": "white", "kicker": "Em uma frase",
    "title": "O que é a *DRE* da clínica?",
    "text": "É o relatório que mostra quanto a clínica faturou, quanto gastou com materiais, laboratório, repasses, equipe e impostos, e quanto sobrou de lucro.",
    "box": "Agenda cheia mostra movimento. A DRE mostra resultado.",
}, """
DRE é a Demonstração do Resultado do Exercício.

Em uma frase: é o relatório que mostra quanto a clínica faturou, quanto gastou com materiais, laboratório, repasses, equipe e impostos, e quanto sobrou de lucro. É ela que responde se a clínica está dando resultado, e não apenas com a agenda cheia.

Se você nunca recebeu a DRE da sua clínica, peça ao seu contador.

Salve e compartilhe com um colega dono de clínica.

#clinicaodontologica #dre #gestaofinanceira #contabilidadeparadentistas
"""),

car("2027-01-22", "saida-de-socio", [
    C("Societário", "Sócio saindo da clínica: o que *formalizar*", "Saída sem documentação gera conflito e responsabilidade anos depois.", "4 etapas para uma saída segura"),
    S("01", "Alteração *contratual*", ["A saída precisa ser registrada por alteração do contrato social.", "Até o registro, o dentista continua aparecendo como sócio da clínica."]),
    S("02", "Apuração de *haveres*", ["É o cálculo do valor que o sócio que sai tem a receber.", "Deve seguir o contrato social, normalmente com base em um balanço levantado na data da saída."]),
    S("03", "Pacientes e *responsabilidade técnica*", ["Defina como ficam os tratamentos em andamento e quem assume a responsabilidade técnica no CRO, se for o caso."]),
    S("04", "Responsabilidade", ["Pelo Código Civil, o sócio que se retira continua respondendo pelas obrigações sociais anteriores por até 2 anos após a averbação da saída."], box="Contas bancárias, procurações, certificados digitais e cadastros também precisam ser atualizados."),
    A("Saída bem feita protege os dois lados", "Envolva o contador e o advogado antes de assinar qualquer acordo.", "Envie para quem está passando por isso"),
], """
A saída de um sócio é um dos momentos mais delicados de uma clínica, e o que não é formalizado costuma virar conflito.

Quatro pontos: alteração do contrato social registrada, apuração de haveres conforme o contrato, definição dos tratamentos em andamento e da responsabilidade técnica no CRO, e atenção à responsabilidade. Pelo Código Civil, o sócio que sai continua respondendo pelas obrigações anteriores por até 2 anos após a averbação.

Também é preciso atualizar contas bancárias, procurações, certificados e cadastros.

Salve e compartilhe com quem está passando por isso.

#clinicaodontologica #societario #saidadesocio #gestaodeclinicas #contabilidadeparadentistas
"""),

img("2027-01-27", "institucional-onde-voce-esta", {
    "theme": "navy", "kicker": "Como trabalhamos",
    "title": "Contabilidade para *clínicas odontológicas*, com um contador *presente*",
    "text": "• Atendimento por WhatsApp e videochamada\n• Visitas à sua clínica quando necessário\n• Regime, repasses, convênios e Reforma no mesmo lugar",
    "box": "Você não precisa sair da clínica para ter um contador perto.",
}, """
Na Smartcontax, a contabilidade é 100% digital e focada em clínicas odontológicas e da área da saúde.

Falamos por WhatsApp e videochamada, e vamos até a sua clínica quando faz sentido. Cuidamos de regime tributário, repasses aos dentistas, convênios, folha da equipe e adaptação à Reforma Tributária, com foco em clareza nos números e segurança fiscal.

Quer conhecer melhor? Fale com a gente pelo link da bio.

#contabilidadeparadentistas #clinicaodontologica #contabilidadedigital #smartcontax
"""),

]
