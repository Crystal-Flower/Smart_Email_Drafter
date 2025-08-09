import ollama
import helper

def Main():
    data , name = helper.get_unread_messages()
    for sender,sub,body, in data:
        mail = body
        context = f"Sender : {sender}\nSubject: {sub}\nDraft the mail by signing it off as {name}"
        prompt = f"""You are an assistant helping draft professional email replies.
    
    Based on the incoming email content provided below, generate a clear, polite, and context-aware reply.
    
    Consider the following:
    
    Match the tone of the original email (formal, semi-formal, or casual)
    
    Acknowledge key points or questions raised
    
    Provide specific responses, next steps, or clarifications
    
    Keep the response concise and well-structured
    
    Incoming Email:
    {mail.strip() if mail else ""}
    
    Additional Context (if any):
    {context}
    
    Your Reply Should:
    
    Begin with an appropriate greeting
    
    Address the sender's concerns or requests
    
    Include any necessary follow-up actions or deadlines
    
    Close with a professional sign-off
    
    Output:
    A ready-to-send email reply. no introduction no outro just the desired output.
    """
        response = ollama.generate("llama3.2",prompt).response
        helper.generate_draft(sender,response,sub)
        print(f"completed mail from {sender}")
        print("-"*40)