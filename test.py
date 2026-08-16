def check_temps(temperatures):
    for i in temperatures:
        if i < 0:
            return True
    return False

print(check_temps([12, 15, 8, -2, 5]))  # Should print True
print(check_temps([10, 14, 22, 18]))   # Should print False