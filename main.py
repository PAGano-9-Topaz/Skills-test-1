from pyscript import display, document



def sample_function(e):

    # Menu is the list we place ahead of time.
    menu = [
        ("check1", "Beef Kaldereta"),
        ("check2", "Ice tea"),
        ("check3", "Pork Sisig"),
        ("check4", "Plain rice"),
        ("check5", "Bicol express"),
    ]
    # Right now, total and all_items are empty, and ready to be filled with values.
    total = 0 
    all_items = []
    # check_id pertains to the 1st part of the list we made earlier, and item_name being the second,. Ex. Check_id = check1 and item_name = beef kaldereta. The whole code itself runs loops checking each check_id and item_name
    for check_id, item_name in menu: 
        cb = document.getElementById(check_id)
        if cb.checked: 
            # in total, '+' means to add all of the values. 'int' turns the string value we added earlier in HTML into an integer (number)
            total += int(cb.value) 
            # append just means to add onto a list, so append would add all item_names together.
            all_items.append(item_name)

    # customer info
    data1 = document.getElementById('input1').value
    data2 = document.getElementById('input2').value
    data3 = document.getElementById('input3').value
    # all_items: means that, if all_items have a checkbox checked, them message = "blah blah", but if you didnt check anything, the error response appears.
    if all_items: 
                # .join simply means to join all items into 1 string value, which is ", "
                items_str = ", ".join(all_items)
                message = f"""
Order for: {data1} 
Contact Number: {data2}
Address: {data3}
\n
Items ordered: {items_str}
Total:P{total}
"""
    else: 
          message = f"""No Items had been selected, please select items before generating your order"""
    document.getElementById("output").innerText = message