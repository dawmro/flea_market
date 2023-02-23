from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item

from .models import Conversation
from .forms import ConversationMessageForm

# Create your views here.

# new conversation view, pk of item
@login_required
def new_conversation(request, item_pk):
    # get item from database
    item = get_object_or_404(Item, pk=item_pk)

    # don't allow item owner to visit this page
    if item.created_by == request.user:
        return redirect('dashboard:index')

    # get all conversations connected to this item when current user is member of conversation
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    # check if conversation about item with item owner and current user already exists
    if conversations:
        pass
        # TODO
        # redirect to conversation page

    # check if form has been submited, handle POST request
    if request.method == 'POST':
        # get data from form
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # create new conversation
            conversation = Conversation.objects.create(item=item)
            # add current user to members of conversation
            conversation.members.add(request.user)
            # add owner of item to members of conversation
            conversation.members.add(item.created_by)
            # save conversation
            conversation.save()

            # create message for conversation, but don't save it to db yet to avoid error
            conversation_message = form.save(commit=False)
            # link message to the conversation
            conversation_message.conversation = conversation
            # who created message
            conversation_message.created_by = request.user
            # save conversation_message and commit to db 
            conversation_message.save()

            # redirect to item detail
            return redirect('item:detail', pk=item_pk)
    
    # handle GET request
    else:
        # create empty form
        form = ConversationMessageForm()

    context = {
        'form': form
    }
    #render template for new conversation
    return render(request, 'conversation/new.html', context)    


# inbox view
@login_required
def inbox(request):
    # get all conversations that current user is member of
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    context = {
        'conversations': conversations
    }
    return render(request, 'conversation/inbox.html', context)


# conversation detail view, pk of conversation
@login_required
def detail(request, pk):
    # get conversation that current user is member of, where pk is pk of this conversation
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    # check if form has been submited, handle POST request
    if request.method == 'POST':
        # get data from form
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            # link to current conversation
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)

    # handle GET request
    else:
        # create empty instance
        form = ConversationMessageForm()

    context = {
        'conversation': conversation,
        'form': form,
    }
    return render(request, 'conversation/detail.html', context)
