from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
import os

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Abel Makkonen Tesfaye[a] (Amharic: አቤል መኮንን ተስፋዬ; born February 16, 1990), known professionally as the Weeknd, is a Canadian singer-songwriter, record producer, and actor.[2][3] Regarded as an influential figure in popular music, he is known for his light-lyric tenor vocal range and falsetto, as well as his alternative R&B sound. His accolades include four Grammy Awards, 20 Billboard Music Awards, 22 Juno Awards, six American Music Awards, three MTV Video Music Awards, and a Latin Grammy Award.

    Tesfaye began releasing music anonymously in 2009. After co-founding the record label XO, he released three mixtapes—House of Balloons, Thursday, and Echoes of Silence—in 2011. He signed with Republic Records to compile the mixtapes into the compilation album Trilogy (2012), and release his debut studio album, Kiss Land (2013) the following year. Following collaborations and film soundtrack contributions from 2013 and 2014, Tesfaye blended alternative R&B with pop on his second and third studio albums, Beauty Behind the Madness (2015) and Starboy (2016); both debuted atop the US Billboard 200 and featured the Billboard Hot 100 number-one singles "Can't Feel My Face", "The Hills", "Starboy", and "Die for You".

    Tesfaye returned to his alternative R&B sound for his debut EP, My Dear Melancholy (2018), featuring the US top-ten single "Call Out My Name". He began an album trilogy based on three time points, starting with the dream pop and new wave-inspired album After Hours (2020), which spawned the chart-topping singles "Heartless" and "Save Your Tears", as well as "Blinding Lights"—the best-performing song in the Billboard Hot 100's history and the most-streamed song on Spotify. The trilogy's latter two installments, Dawn FM (2022) and Hurry Up Tomorrow (2025), featured the US top-ten singles, "Take My Breath" and "Timeless". In 2023, he co-created and starred in the controversial HBO drama series The Idol, which was received as a critical failure.

    Tesfaye is one of the best-selling artists of all time with estimated sales of over 75 million units,[4] and has amassed eight diamond-certified singles from the RIAA.[5] Time named him one of the world's most influential people in 2020. After Hours would go on to be the most-streamed R&B album in history, while his longest-spanning After Hours til Dawn Tour set the record for the highest-grossing R&B tour in history. Tesfaye co-founded the record label XO in 2011 and hosted the Apple Music 1 radio show Memento Mori from 2018 to 2022. In 2020, he launched the incubator HXOUSE of which he serves as a sleeping partner, and was appointed goodwill ambassador for the World Food Programme in 2021. He has also donated to various causes and expressed activism over racial equality and food security.    
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    3. estimate his date and cause of death
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatGroq(temperature=1, model="llama-3.3-70b-versatile")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
