from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

#Tool: Add two numbers
@mcp.tool()
def add_numbers(a:int,b:int) -> int:
    """Add two integer numbers together.
    Args:
    a: first number
    b:second number
    
    Return:Sum of a and b"""
    return a+b


#Tool : Generate a random number
@mcp.tool()
def random_number(min_value : int =1 , max_value :int =100) -> int:
    """Generate a random number within the range
    
    args:
        min_value : minimum value of the range
        max_value : maximum value of the range
        
    return:
        Random integer within the range"""
    return random.randint(min_value,max_value)


#Resource : Server info
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server"""
    info = {
        'name' : "Simple calculator server",
        'version' : '1.0.0',
        'info' : 'A basic MCP server with math tool',
        'tools' : ['add_numbers','random_number'],
        'author' : 'Ekaagra Agarwal'
    }
    return json.dumps(info, indent= 2)

if __name__ == "__main__":
    mcp.run(transport = 'http' , host = '0.0.0.0' , port  = 8000)
