class ServicoPetshop:
    def __init__(self, nomeCliente, animal,nomeAnimal, racaAnimal, generoAnimal,nomeDoutor, procedimento, dataProcedimento):
        self.nomeCliente = nomeCliente
        self.animal = animal
        self.nomeAnimal = nomeAnimal
        self.racaAnimal = racaAnimal
        self.generoAnimal = generoAnimal
        self.nomeDoutor = nomeDoutor
        self.procedimento = procedimento
        self.dataProcedimento = dataProcedimento

class Agendamento:
    def __init__(self):
        self.servicos = []

    def agendar_servico(self, servico):
        self.servicos.append(servico)
        print("Serviço agendado com sucesso!")

    def visualizar_datas(self):
        datas = {}
        for servico in self.servicos:
            if servico.dataProcedimento not in datas:
                datas[servico.dataProcedimento] = [servico.nomeCliente]
            else:
                datas[servico.dataProcedimento].append(servico.nomeCliente)
       
        print("\nDatas dos Procedimentos:")
        for data, clientes in datas.items():
            print(f"{data}: {', '.join(clientes)}")

def main():
    agendamento = Agendamento()

    while True:
        print("\n=== Menu ===")
        print("1. Agendar Serviço")
        print("2. Exibir Agendamentos")
        print("3. Visualizar Datas dos Procedimentos")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nomeCliente = input("Digite o nome do cliente: ")
            animal = input("Digite qual animal: ")
            nomeAnimal = input("Digite o nome do animal: ")
            racaAnimal = input("Digite a raça do animal: ")
            generoAnimal = input("Digite o genêro do animal: ")
            nomeDoutor = input("Digite o nome do doutor: ")
            procedimento = input("Digite o procedimento a ser realizado: ")
            dataProcedimento = input("Digite a data do procedimento (DD/MM/AAAA): ")
            novo_servico = ServicoPetshop(nomeCliente, animal, nomeAnimal, racaAnimal, generoAnimal, nomeDoutor, procedimento, dataProcedimento)
            agendamento.agendar_servico(novo_servico)

        elif escolha == "2":
            print("\nAgendamentos:")
            for i, servico in enumerate(agendamento.servicos, start=1):
                print(f"{i}. Cliente: {servico.nomeCliente}, Animal: {servico.animal}, Nome do animal: {servico.nomeAnimal}, Genêro: {servico.generoAnimal}, Raça: {servico.racaAnimal}, Doutor: {servico.nomeDoutor}, Procedimento: {servico.procedimento}, Data do Procedimento: {servico.dataProcedimento}")

        elif escolha == "3":
            agendamento.visualizar_datas()

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()