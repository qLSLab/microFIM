import os
import sys

""" Functions to set microFim directories. For simpilicty, to use this functions
into a Python script or Python Interpreter, import microFim.microdir as md """

# set directories

def set_inputs_dir(inputs_dir = 'input'):
    """ Set inputs directory """
    current_dir = os.getcwd()
    i_dir = os.path.join(current_dir, inputs_dir)
    #os.mkdir(i_dir)
    return i_dir

def set_outputs_dir(outputs_dir = 'output'):
    """ Set outputs directory """
    current_dir = os.getcwd()
    o_dir = os.path.join(current_dir, outputs_dir)
    #os.mkdir(i_dir)
    return o_dir
