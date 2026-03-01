from pyscript import display, document

def team_checker(e):
    # Getting user inputs
    name = document.getElementById("name").value

    # Checking radio button selections
    # I used .checked to determine if the radio button is selected
    registration_yes = document.getElementById("ryes").checked
    registration_no = document.getElementById("rno").checked

    medical_yes = document.getElementById("myes").checked
    medical_no = document.getElementById("mno").checked

    # Error message for empty name field
    if name == "":
        display("Please enter your name.", target="team_output", append=False)

    # I used or operator to check if either registration or medical requirement is not met which ensures the user completes both requirements
    if registration_no or medical_no:
        if registration_no:
            display("Please complete the online registration form given to you.", target="team_output", append=False)
            document.getElementById("team_logo").src = ""
        elif medical_no:
            display("Please secure a medical clearance from the school clinic.", target="team_output", append=False)
            document.getElementById("team_logo").src = ""
        elif registration_no and medical_no:
            display("Please complete the necessary requirements.", target="team_output", append=False)
            document.getElementById("team_logo").src = ""

    # If both requirements are met, check for team assignment
    # I nested the if statements to ensure both requirements are met before proceeding to team assignment
   
    if registration_yes:
        if medical_yes:
            # document.getElementById().value is used to get the selected level and section
            level = document.getElementById("level").value
            section = document.getElementById("section").value

             # I nested the level and section if statements to ensure the correct team assignment based on both inputs
             # I used f-strings to format the welcome message with the user's name and team
            if level =="7":
                if section =="Emerald":
                    display(f"Welcome to Blue Bears, {name}!", target="team_output", append=False)
            
            # document.getElementById().src is used to change the image source based on team assignment. In addition, it also removes the team logo if N/A is displayed or an error.
                    document.getElementById("team_logo").src = "bear.png"
            
                elif section =="Ruby":
                    display(f"Welcome to Yellow Tigers, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "tiger.png"
                
                elif section =="Sapphire":
                    display(f"Welcome to Red Bulldogs, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bulldog.png"
                
                elif section =="Topaz":
                    display(f"Welcome to Green Hornets, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "hornet.png"
                    
                elif section =="Jade":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Luna":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Amorsolo":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Jose":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Tinio":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                    
                else:
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""


            elif level =="8":
                if section =="Emerald":
                    display(f"Welcome to Yellow Tigers, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "tiger.png"
                elif section =="Ruby":
                    display(f"Welcome to Red Bulldogs, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bulldog.png"
                elif section =="Sapphire":
                    display(f"Welcome to Green Hornets, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "hornet.png"
                elif section =="Topaz":
                    display(f"Welcome to Blue Bears, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bear.png"
                elif section =="Jade":
                    display(f"Welcome to Blue Bears, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bear.png"
                elif section =="Luna":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Amorsolo":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Jose":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Tinio":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                    
                else:
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                


            elif level =="9":
                if section =="Emerald":
                    display(f"Welcome to Green Hornets, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "hornet.png"
                elif section =="Ruby":
                    display(f"Welcome to Blue Bears, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bear.png"
                elif section =="Sapphire":
                    display(f"Welcome to Yellow Tigers, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "tiger.png"
                elif section =="Topaz":
                    display(f"Welcome to Red Bulldogs, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bulldog.png"
                elif section =="Jade":
                    display(f"Welcome to Green Hornets, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "hornet.png"

                elif section =="Luna":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Amorsolo":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Jose":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Tinio":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                    
                else:
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""


            elif level =="10":
                if section =="Emerald":
                    display(f"Welcome to Red Bulldogs, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bulldog.png"
                elif section =="Ruby":
                    display(f"Welcome to Green Hornets, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "hornet.png"
                elif section =="Sapphire":
                    display(f"Welcome to Yellow Tigers, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "tiger.png"
                elif section =="Topaz":
                    display(f"Welcome to Blue Bears, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bear.png"
                elif section =="Jade":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Luna":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Amorsolo":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Jose":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Tinio":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                    
                else:
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

            elif level =="11":
                if section =="Luna":
                    display(f"Welcome to Yellow Tigers, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "tiger.png"
                
                elif section =="Amorsolo":
                    display(f"Welcome to Green Hornets, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "hornet.png"
                
                elif section =="Emerald":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Ruby":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Sapphire":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Topaz":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Jade":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Jose":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Tinio":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                else:
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

            elif level =="12":
                if section =="Jose":
                    display(f"Welcome to Blue Bears, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bear.png"
                
                elif section =="Tinio":
                    display(f"Welcome to Red Bulldogs, {name}!", target="team_output", append=False)
                    document.getElementById("team_logo").src = "bulldog.png"
                
                elif section =="Emerald":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Ruby":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Sapphire":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Topaz":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                elif section =="Jade":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Luna":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

                elif section =="Amorsolo":
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                
                else:
                    display("N/A", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""


            # I copied it here so it won't be overwritten by the previous if statement
            if name == "":
                display("Please enter your name.", target="team_output", append=False)
                document.getElementById("team_logo").src = ""

            # This is just a failsafe in case the one above gets overwritten
            elif registration_no or medical_no:
                if registration_no:
                    display("Please complete the online registration form given to you.", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                elif medical_no:
                    display("Please secure a medical clearance from the school clinic.", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""
                elif registration_no and medical_no:
                    display("Please complete the necessary requirements.", target="team_output", append=False)
                    document.getElementById("team_logo").src = ""

    