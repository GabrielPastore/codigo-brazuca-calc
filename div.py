def div(a:float, b:float):
    result = a/b
    return result

if __name__ == "__main__":
    import sys
    
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    
    try:
        print(div(a,b))
    except:
        print('Denominador 0')
