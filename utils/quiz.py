from enum import Enum
from typing import List


class QuizDifficulty(Enum):
    EASY = 'Fácil'
    MEDIUM = 'Médio'
    HARD = 'Difícil'


class Quiz:
    def __init__(self):
        pass

    def get_questions(self, difficulty: QuizDifficulty) -> List[dict]:
        return self._get_questions(difficulty)

    @staticmethod
    def _get_questions(difficulty: QuizDifficulty) -> List[dict]:
        questions: List[dict] = []

        if difficulty == QuizDifficulty.EASY:
            questions = [
                {
                    'question': 'O que é uma classe em Java?',
                    'items': {
                        'Função que executa código': False,
                        'Modelo para objetos': True,
                        'Estrutura de dados': False,
                        'Biblioteca Java': False,
                    }
                },
                {
                    'question': 'O que significa encapsulamento?',
                    'items': {
                        'Criar métodos estáticos': False,
                        'Extensão de classes': False,
                        'Organizar pacotes': False,
                        'Esconder dados dentro da classe': True,
                    }
                },
                {
                    'question': 'Qual a finalidade de um construtor em Java?',
                    'items': {
                        'Exibir dados na tela': False,
                        'Criar um método estático': False,
                        'Inicializar objetos': True,
                        'Criar um arquivo de configuração': False,
                    }
                },
                {
                    'question': 'O que é herança em Java?',
                    'items': {
                        'Quando uma classe herda propriedades de outra': True,
                        'Quando dois objetos compartilham dados': False,
                        'Quando uma classe é final': False,
                        'Quando o método é privado': False,
                    }
                },
                {
                    'question': 'Como se chama um método de uma classe em Java?',
                    'items': {
                        'Usando o nome da classe': False,
                        'Usando o operador .': True,
                        'Com o operador new': False,
                        'Usando o operador ++': False,
                    }
                },
                {
                    'question': 'O que é uma interface em Java?',
                    'items': {
                        'Uma classe abstrata': False,
                        'Um contrato de métodos': True,
                        'Uma função externa': False,
                        'Um tipo de variável': False,
                    }
                },
                {
                    'question': 'Em Java, o que é o método toString()?',
                    'items': {
                        'Método para criar uma cópia do objeto': False,
                        'Método para comparar objetos': False,
                        'Método para converter objetos em texto': True,
                        'Método para declarar variáveis': False,
                    }
                },
                {
                    'question': 'O que significa o termo "polimorfismo"?',
                    'items': {
                        'Métodos com o mesmo nome, mas comportamentos diferentes': True,
                        'Criar múltiplas instâncias de uma classe': False,
                        'Estabelecer hierarquias entre objetos': False,
                        'Usar uma variável para múltiplos tipos': False,
                    }
                },
                {
                    'question': 'O que é o operador instanceof em Java?',
                    'items': {
                        'Cria uma nova instância de um objeto': False,
                        'Verifica se uma variável é nula': False,
                        'Compara duas instâncias de objetos': False,
                        'Verifica o tipo de uma variável': True,
                    }
                },
                {
                    'question': 'Qual é a palavra-chave para herdar em Java?',
                    'items': {
                        'super': False,
                        'this': False,
                        'static': False,
                        'extends': True,
                    }
                },
            ]

        elif difficulty == QuizDifficulty.MEDIUM:
            questions = [
                {
                    'question': 'O que é o modificador "final" em Java?',
                    'items': {
                        'Define um método que será sobrecarregado': False,
                        'Define algo imutável ou final': True,
                        'Define uma constante': False,
                        'Define uma classe abstrata': False,
                    }
                },
                {
                    'question': 'Qual a diferença entre "super" e "this" em Java?',
                    'items': {
                        'super chama o construtor da classe pai e this chama a classe atual': True,
                        'this chama o método estático e super chama o método de instância': False,
                        'super é para acessar variáveis locais, this é para acessar globais': False,
                        'this é usado para herança e super para objetos estáticos': False,
                    }
                },
                {
                    'question': 'O que é uma classe abstrata em Java?',
                    'items': {
                        'Uma classe que não pode ser instanciada diretamente': True,
                        'Uma classe que possui apenas métodos estáticos': False,
                        'Uma classe que não possui herança': False,
                        'Uma classe que não pode ter métodos': False,
                    }
                },
                {
                    'question': 'Como se cria uma exceção personalizada em Java?',
                    'items': {
                        'Usando a palavra-chave throw diretamente': False,
                        'Usando a palavra-chave extends': False,
                        'Criando uma variável do tipo Exception': False,
                        'Criando uma classe que estende Exception': True,
                    }
                },
                {
                    'question': 'O que é o conceito de "overriding" em Java?',
                    'items': {
                        'Sobrecarga de métodos': False,
                        'Quando um método é privado': False,
                        'Substituir um método da classe pai na classe filha': True,
                        'Quando um método é chamado com super': False,
                    }
                },
                {
                    'question': 'O que são métodos estáticos em Java?',
                    'items': {
                        'Métodos que alteram o estado da classe': False,
                        'Métodos que retornam dados do banco de dados': False,
                        'Métodos que pertencem à classe, não à instância': True,
                        'Métodos que não podem ser chamados dentro da classe': False,
                    }
                },
                {
                    'question': 'Qual é a principal diferença entre List e Set em Java?',
                    'items': {
                        'List não permite elementos duplicados, Set permite': False,
                        'Set não permite elementos duplicados, List permite': True,
                        'List é para objetos, Set para tipos primitivos': False,
                        'Set é mais rápido que List para acesso aleatório': False,
                    }
                },
                {
                    'question': 'O que é o método equals() em Java?',
                    'items': {
                        'Método para comparar dois tipos primitivos': False,
                        'Método para comparar dois objetos': True,
                        'Método para comparar strings somente': False,
                        'Método para converter tipos': False,
                    }
                },
                {
                    'question': 'Qual é a diferença entre "ArrayList" e "LinkedList" em Java?',
                    'items': {
                        'ArrayList é baseado em array, LinkedList em lista duplamente encadeada': True,
                        'ArrayList é mais rápido para inserções, LinkedList para buscas': False,
                        'LinkedList é mais eficiente em acesso sequencial': False,
                        'ArrayList não permite valores nulos': False,
                    }
                },
                {
                    'question': 'O que faz o operador "super" em Java?',
                    'items': {
                        'Acessa variáveis estáticas da classe pai': False,
                        'Chama o método main da classe pai': False,
                        'Instancia objetos dentro da classe pai': False,
                        'Chama métodos ou construtores da classe pai': True,
                    }
                },
            ]

        elif difficulty == QuizDifficulty.HARD:
            questions = [
                {
                    'question': 'Como se realiza a sincronização de threads em Java?',
                    'items': {
                        'Usando a palavra-chave volatile': False,
                        'Usando a classe Thread': False,
                        'Com o método wait() e notify()': False,
                        'Usando a palavra-chave synchronized': True,
                    }
                },
                {
                    'question': 'O que são "design patterns" em Java?',
                    'items': {
                        'Um conjunto de ferramentas para trabalhar com múltiplas threads': False,
                        'Estruturas de dados específicas para cada tipo de aplicação': False,
                        'Soluções reutilizáveis para problemas recorrentes de design de software': True,
                        'Técnicas para compilar código Java mais rápido': False,
                    }
                },
                {
                    'question': 'O que significa a palavra-chave "transient" em Java?',
                    'items': {
                        'Indica que um atributo não será serializado': True,
                        'Indica que um método não pode ser sobrecarregado': False,
                        'Indica que a variável não será visível em subclasses': False,
                        'Impede que a variável seja modificada': False,
                    }
                },
                {
                    'question': 'O que é um "singleton" em Java?',
                    'items': {
                        'Uma classe que pode ser instanciada múltiplas vezes': False,
                        'Um método estático usado para criar objetos': False,
                        'Um padrão de design que garante uma única instância de uma classe': True,
                        'Uma classe que utiliza a palavra-chave final': False,
                    }
                },
                {
                    'question': 'O que significa a palavra-chave "volatile" em Java?',
                    'items': {
                        'Aumenta a eficiência das variáveis estáticas': False,
                        'Indica que uma variável pode ser alterada por diferentes threads': True,
                        'Indica que um método é privado e não pode ser acessado fora da classe': False,
                        'Define que uma variável é constante': False,
                    }
                },
                {
                    'question': 'O que são "callbacks" em Java?',
                    'items': {
                        'Funções de inicialização chamadas ao iniciar a aplicação': False,
                        'Funções que retornam valores quando chamadas': False,
                        'Funções passadas como parâmetros para serem chamadas em outro contexto': True,
                        'Funções que fazem a leitura de arquivos': False,
                    }
                },
                {
                    'question': 'O que é o padrão de design "Factory" em Java?',
                    'items': {
                        'Método para configurar objetos antes de sua criação': False,
                        'Método para criar objetos sem expor a lógica de criação': True,
                        'Método que gera um objeto de forma recursiva': False,
                        'Método que verifica se o objeto já existe antes de criá-lo': False,
                    }
                },
                {
                    'question': 'Qual é a diferença entre "Serializable" e "Externalizable" em Java?',
                    'items': {
                        'Serializable é mais eficiente em performance que Externalizable': False,
                        'Externalizable é utilizado apenas para arquivos binários': False,
                        'Serializable permite controle de fluxo de dados durante a serialização': False,
                        'Externalizable permite controle total sobre a serialização, Serializable não': True,
                    }
                },
                {
                    'question': 'Como funciona o "garbage collector" em Java?',
                    'items': {
                        'Remove objetos não utilizados da memória automaticamente': True,
                        'Libera memória manualmente quando o programador chama o método': False,
                        'Aloca memória para novos objetos automaticamente': False,
                        'Verifica erros de programação em tempo de execução': False,
                    }
                },
                {
                    'question': 'O que é o "Java Reflection" e para que serve?',
                    'items': {
                        'Permite executar código Java de forma assíncrona': False,
                        'Permite compilar código Java em tempo de execução': False,
                        'Permite realizar chamadas de rede de maneira eficiente': False,
                        'Permite inspecionar e modificar a estrutura de classes em tempo de execução': True,
                    }
                },
            ]

        return questions
