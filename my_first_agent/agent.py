from google.adk.agents.llm_agent import Agent

root_agent = Agent( #root_agent no se cambia, eso lo busca el adk
    model='gemini-3.5-flash',
    name='='math_tutor_agent', #nombre mas descriptivo 
    description='Este agente va a ayudar a los estudiantes a aprender álgebra guiándolos a través de los pasos para la resolución de problema',
    instruction='Eres un tutor de matemáticas paciente. Ayuda a los estudiantes con
los problemas de álgebra', 
# el parámetro instruction le dice a este agente cómo comportarse y
responder.
)
