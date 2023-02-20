# from flask import Flask, render_template, send_file

from asyncio import SendfileNotAvailableError


def index():
    return index.html

def download():
    try:
        return ("static/vadim_resume.pdf",as_attachment=True)
    except Exception as e:
        return str(e)

