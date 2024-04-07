def unique_email_adress(emails:list)->list:
    output = []
    for email in emails:
        local_name, Domain_name = email.split("@")
        local_name = local_name.split("+")[0]
        local_name = local_name.replace(".","")
        output.append(local_name + "@" + Domain_name)
    return len(set(output))