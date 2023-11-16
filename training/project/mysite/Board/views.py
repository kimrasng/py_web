from django.shortcuts import render, redirect, get_object_or_404
from Board.models import Board
from Board.forms import BoardCreatrForm, BoardUpdateForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from config import settings
import os

# Create your views here.

class BoardUpdate(UpdateView):
    model = Board
    form_class = BoardUpdateForm
    template_name = 'Board/board_form_update.html'


@login_required(login_url='common:login')
def BoardDelete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user != board.author:
        return redirect('Board:detail', pk=pk)
    if board.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, board.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    board.delete()
    return redirect('Board:list')


class BoardCreate(CreateView):
    model = Board
    form_class = BoardCreatrForm
    template_name = 'Board/board_form.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/Board')


class BoardList(ListView):
    model = Board
    template_name = 'Board/board_list.html'
    ordering = '-pk'
    paginate_by = 10

class BoardDetail(DetailView):
    model = Board
    template_name = 'Board/board_detail.html' 


