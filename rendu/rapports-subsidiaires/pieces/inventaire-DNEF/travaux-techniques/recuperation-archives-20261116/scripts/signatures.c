#include <stdint.h>
#include <stddef.h>
#include <string.h>

#define MAX_NODES 2048
static int transitions[MAX_NODES][256], failure[MAX_NODES], nodes;
static uint64_t outputs[MAX_NODES];
static unsigned char fold(unsigned char c) {return c >= 'A' && c <= 'Z' ? c + 32 : c;}

int initialize(const unsigned char **patterns, const size_t *lengths, int count) {
    if(count > 63) return -1;
    memset(transitions,0,sizeof(transitions)); memset(failure,0,sizeof(failure)); memset(outputs,0,sizeof(outputs));nodes=1;
    for(int p=0;p<count;p++) {
        int s=0;
        for(size_t j=0;j<lengths[p];j++) {
            unsigned char c=fold(patterns[p][j]);
            if(!transitions[s][c]) {if(nodes==MAX_NODES)return -2; transitions[s][c]=nodes++;}
            s=transitions[s][c];
        }
        outputs[s] |= ((uint64_t)1 << p);
    }
    int queue[MAX_NODES], front=0, back=0;
    for(int c=0;c<256;c++) if(transitions[0][c]) queue[back++]=transitions[0][c];
    while(front<back) {
        int s=queue[front++];
        for(int c=0;c<256;c++) {
            int t=transitions[s][c];
            if(t) {failure[t]=transitions[failure[s]][c];outputs[t]|=outputs[failure[t]];queue[back++]=t;}
            else transitions[s][c]=transitions[failure[s]][c];
        }
    }
    return nodes;
}

long scan(const unsigned char *data,size_t length,int *pattern_ids,size_t *end_offsets,size_t capacity) {
    int state=0;size_t found=0;
    for(size_t i=0;i<length;i++) {
        state=transitions[state][fold(data[i])];
        uint64_t mask=outputs[state];
        while(mask) {
            if(found>=capacity)return -1;
            int id=__builtin_ctzll(mask);pattern_ids[found]=id;end_offsets[found]=i+1;found++;
            mask &= mask-1;
        }
    }
    return (long)found;
}
